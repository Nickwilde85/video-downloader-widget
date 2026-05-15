import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading, os
from pathlib import Path

try:
    import yt_dlp
except:
    yt_dlp = None

def check_ffmpeg():
    try:
        import subprocess
        return subprocess.run(['ffmpeg', '-version'], capture_output=True, timeout=5).returncode == 0
    except:
        return False

class App:
    def __init__(self, root):
        self.root = root
        root.title("Video Downloader")
        root.geometry("700x600")
        root.resizable(False, False)
        
        self.lang = {'en': {'title': 'Video Downloader', 'url': 'Video URL', 'quality': 'Quality', 
                           'folder': 'Folder', 'choose': 'Choose Folder', 'download': 'Download',
                           'ready': 'Ready', 'downloading': 'Downloading', 'complete': 'Complete!',
                           'failed': 'Failed', 'lang': 'Language', 'theme': 'Theme'},
                    'ru': {'title': 'Загрузчик Видео', 'url': 'Ссылка', 'quality': 'Качество',
                           'folder': 'Папка', 'choose': 'Выбрать', 'download': 'Скачать',
                           'ready': 'Готов', 'downloading': 'Скачивание', 'complete': 'Готово!',
                           'failed': 'Ошибка', 'lang': 'Язык', 'theme': 'Тема'}}
        
        self.themes = {'Purple': {'bg': '#1a1a2e', 'bg2': '#16213e', 'accent': '#9d4edd', 'hover': '#c77dff',
                                  'text': '#eaeaea', 'text2': '#a0a0a0', 'ok': '#06ffa5', 'err': '#ff006e'},
                      'Blue': {'bg': '#0d1b2a', 'bg2': '#1b263b', 'accent': '#3a86ff', 'hover': '#5a9fff',
                              'text': '#e0e1dd', 'text2': '#9a9a9a', 'ok': '#06ffa5', 'err': '#ef233c'},
                      'Green': {'bg': '#1b2021', 'bg2': '#2d3436', 'accent': '#00b894', 'hover': '#00d9a5',
                               'text': '#dfe6e9', 'text2': '#95a5a6', 'ok': '#55efc4', 'err': '#ff7675'},
                      'Pink': {'bg': '#2d132c', 'bg2': '#3d1e33', 'accent': '#ee4c7c', 'hover': '#ff6b9d',
                              'text': '#f8f9fa', 'text2': '#adb5bd', 'ok': '#51cf66', 'err': '#ff6b6b'}}
        
        self.cur_lang = 'en'
        self.cur_theme = 'Purple'
        self.c = self.themes[self.cur_theme]
        root.configure(bg=self.c['bg'])
        self.path = str(Path.home() / "Downloads")
        self.ffmpeg = check_ffmpeg()
        self.ui()
    
    def t(self, k): return self.lang[self.cur_lang][k]
    def ch_lang(self, l): self.cur_lang = l; self.refresh()
    def ch_theme(self, t): self.cur_theme = t; self.c = self.themes[t]; self.refresh()
    def refresh(self):
        for w in self.root.winfo_children(): w.destroy()
        self.root.configure(bg=self.c['bg'])
        self.ui()

    
    def ui(self):
        # Top
        top = tk.Frame(self.root, bg=self.c['bg'])
        top.pack(fill=tk.X, padx=30, pady=(15,0))
        tk.Label(top, text=self.t('lang'), font=("Segoe UI",9), bg=self.c['bg'], fg=self.c['text2']).pack(side=tk.LEFT, padx=(0,5))
        self.lv = tk.StringVar(value=self.cur_lang)
        lc = ttk.Combobox(top, textvariable=self.lv, values=['en','ru'], state="readonly", width=5)
        lc.pack(side=tk.LEFT, padx=(0,20))
        lc.bind('<<ComboboxSelected>>', lambda e: self.ch_lang(self.lv.get()))
        tk.Label(top, text=self.t('theme'), font=("Segoe UI",9), bg=self.c['bg'], fg=self.c['text2']).pack(side=tk.LEFT, padx=(0,5))
        self.tv = tk.StringVar(value=self.cur_theme)
        tc = ttk.Combobox(top, textvariable=self.tv, values=list(self.themes.keys()), state="readonly", width=8)
        tc.pack(side=tk.LEFT)
        tc.bind('<<ComboboxSelected>>', lambda e: self.ch_theme(self.tv.get()))
        
        # Title
        tk.Label(self.root, text=self.t('title'), font=("Segoe UI",22,"bold"), bg=self.c['bg'], fg=self.c['accent'], pady=15).pack()
        
        # URL
        uc = tk.Frame(self.root, bg=self.c['bg'])
        uc.pack(fill=tk.X, padx=30, pady=10)
        tk.Label(uc, text=self.t('url'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text2']).pack(anchor=tk.W, pady=(0,5))
        ef = tk.Frame(uc, bg=self.c['bg2'])
        ef.pack(fill=tk.X)
        self.url = tk.Entry(ef, font=("Segoe UI",11), bg=self.c['bg2'], fg=self.c['text'], insertbackground=self.c['accent'], relief=tk.FLAT, bd=0)
        self.url.pack(fill=tk.X, padx=15, pady=12)
        self.url.bind('<Return>', lambda e: self.download())
        
        # Settings
        sf = tk.Frame(self.root, bg=self.c['bg'])
        sf.pack(fill=tk.X, padx=30, pady=20)
        tk.Label(sf, text=self.t('quality'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text2']).grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0,15))
        self.qv = tk.StringVar(value="max")
        ttk.Combobox(sf, textvariable=self.qv, values=["max","1080p","720p","480p","360p","audio"], state="readonly", width=12).grid(row=0, column=1, sticky=tk.W)
        tk.Label(sf, text=self.t('folder'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text2']).grid(row=1, column=0, sticky=tk.W, pady=5, padx=(0,15))
        tk.Button(sf, text=self.t('choose'), command=self.choose, bg=self.c['accent'], fg='white', font=("Segoe UI",9), relief=tk.FLAT, padx=15, pady=5, cursor='hand2', activebackground=self.c['hover']).grid(row=1, column=1, sticky=tk.W)
        self.pl = tk.Label(sf, text="Downloads", font=("Segoe UI",8), bg=self.c['bg'], fg=self.c['text2'])
        self.pl.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(5,0))
        
        # Download
        self.db = tk.Button(self.root, text=self.t('download'), command=self.download, bg=self.c['accent'], fg='white', font=("Segoe UI",12,"bold"), relief=tk.FLAT, padx=60, pady=12, cursor='hand2', activebackground=self.c['hover'])
        self.db.pack(pady=20)
        
        # Progress
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TCombobox', fieldbackground=self.c['bg2'], background=self.c['accent'], foreground=self.c['text'])
        s.configure("P.Horizontal.TProgressbar", background=self.c['accent'], troughcolor=self.c['bg2'], borderwidth=0, thickness=8)
        self.pb = ttk.Progressbar(self.root, mode='indeterminate', length=640, style="P.Horizontal.TProgressbar")
        self.pb.pack(pady=10, padx=30)
        
        # Status
        self.st = tk.Label(self.root, text=self.t('ready'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['ok'])
        self.st.pack(pady=10)
    
    def choose(self):
        f = filedialog.askdirectory(initialdir=self.path)
        if f: self.path = f; self.pl.config(text=os.path.basename(f))
    
    def download(self):
        url = self.url.get().strip()
        if not url: messagebox.showwarning("Error", "Enter URL"); return
        if not yt_dlp: messagebox.showerror("Error", "yt-dlp not installed"); return
        threading.Thread(target=self.dl, args=(url,), daemon=True).start()
    
    def dl(self, url):
        self.db.config(state=tk.DISABLED)
        self.pb.start()
        self.upd(self.t('downloading'), self.c['accent'])
        try:
            q = self.qv.get()
            if q == "audio":
                fmt = 'bestaudio/best'
                pp = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}] if self.ffmpeg else []
            elif q == "max":
                fmt = 'bestvideo*+bestaudio/best' if self.ffmpeg else 'best'
                pp = []
            else:
                h = q.replace('p', '')
                fmt = f'bestvideo[height<={h}]+bestaudio/best[height<={h}]' if self.ffmpeg else f'best[height<={h}]'
                pp = []
            opts = {'format': fmt, 'outtmpl': os.path.join(self.path, '%(title)s.%(ext)s'),
                   'progress_hooks': [self.ph], 'postprocessors': pp, 'nocheckcertificate': True,
                   'quiet': True, 'no_warnings': True}
            if self.ffmpeg: opts['merge_output_format'] = 'mp4'
            with yt_dlp.YoutubeDL(opts) as ydl: ydl.download([url])
            self.upd(self.t('complete'), self.c['ok'])
            messagebox.showinfo("Success", f"Saved to:\n{self.path}")
        except Exception as e:
            self.upd(self.t('failed'), self.c['err'])
            messagebox.showerror("Error", str(e))
        finally:
            self.pb.stop()
            self.db.config(state=tk.NORMAL)
    
    def ph(self, d):
        if d['status'] == 'downloading':
            self.upd(f"{self.t('downloading')}: {d.get('_percent_str', 'N/A')}", self.c['accent'])
    
    def upd(self, txt, col): self.st.config(text=txt, foreground=col)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
