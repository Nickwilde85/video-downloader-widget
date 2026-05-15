import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading, os, json
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
        
        self.config_file = Path.home() / ".video_downloader_config.json"
        self.load_config()
        
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
        
        self.c = self.themes[self.cur_theme]
        root.configure(bg=self.c['bg'])
        self.ffmpeg = check_ffmpeg()
        self.ui()
    
    def load_config(self):
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.path = config.get('download_path', str(Path.home() / "Downloads"))
                    self.cur_lang = config.get('language', 'en')
                    self.cur_theme = config.get('theme', 'Pink')
            else:
                self.path = str(Path.home() / "Downloads")
                self.cur_lang = 'en'
                self.cur_theme = 'Pink'
        except:
            self.path = str(Path.home() / "Downloads")
            self.cur_lang = 'en'
            self.cur_theme = 'Pink'
    
    def save_config(self):
        try:
            config = {
                'download_path': self.path,
                'language': self.cur_lang,
                'theme': self.cur_theme
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
        except:
            pass
    
    def t(self, k): return self.lang[self.cur_lang][k]
    def ch_lang(self, l): self.cur_lang = l; self.save_config(); self.refresh()
    def ch_theme(self, t): self.cur_theme = t; self.c = self.themes[t]; self.save_config(); self.refresh()
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
        
        url_label = tk.Label(uc, text=self.t('url'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text2'])
        url_label.pack(anchor=tk.W, pady=(0,5))
        
        # Поддерживаемые платформы
        platforms_text = "✓ YouTube • TikTok • Twitter/X • Instagram • Facebook • Pinterest • Reddit • Vimeo • Dailymotion • 1000+ sites"
        platforms_label = tk.Label(uc, text=platforms_text, font=("Segoe UI",8), bg=self.c['bg'], fg=self.c['text2'])
        platforms_label.pack(anchor=tk.W, pady=(0,5))
        
        # Закругленный фрейм для Entry
        ef = tk.Canvas(uc, height=50, bg=self.c['bg'], highlightthickness=0)
        ef.pack(fill=tk.X)
        ef.create_rounded_rectangle = lambda x1,y1,x2,y2,r=15,**kwargs: ef.create_polygon(
            [x1+r,y1, x1+r,y1, x2-r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y1+r, x2,y2-r, x2,y2-r, x2,y2,
             x2-r,y2, x2-r,y2, x1+r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y2-r, x1,y1+r, x1,y1+r, x1,y1],
            smooth=True, **kwargs)
        ef.create_rounded_rectangle(0, 0, 640, 50, r=15, fill=self.c['bg2'], outline='')
        
        self.url = tk.Entry(ef, font=("Segoe UI",11), bg=self.c['bg2'], fg=self.c['text'], 
                           insertbackground=self.c['accent'], relief=tk.FLAT, bd=0)
        ef.create_window(320, 25, window=self.url, width=610, height=30)
        
        # Placeholder текст
        self.url_placeholder = "Right-click to paste link / ПКМ для вставки ссылки"
        self.url.insert(0, self.url_placeholder)
        self.url.config(fg=self.c['text2'])
        
        def on_focus_in(event):
            if self.url.get() == self.url_placeholder:
                self.url.delete(0, tk.END)
                self.url.config(fg=self.c['text'])
        
        def on_focus_out(event):
            if not self.url.get():
                self.url.insert(0, self.url_placeholder)
                self.url.config(fg=self.c['text2'])
        
        self.url.bind('<FocusIn>', on_focus_in)
        self.url.bind('<FocusOut>', on_focus_out)
        self.url.bind('<Return>', lambda e: self.download())
        self.url.bind('<Button-3>', self.show_menu)
        # Стандартное событие вставки работает с любой раскладкой
        self.url.bind('<<Paste>>', lambda e: None)  # Разрешаем стандартную вставку
        
        # Settings
        sf = tk.Frame(self.root, bg=self.c['bg'])
        sf.pack(fill=tk.X, padx=30, pady=20)
        
        tk.Label(sf, text=self.t('quality'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text']).grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0,15))
        self.qv = tk.StringVar(value="max")
        qc = ttk.Combobox(sf, textvariable=self.qv, values=["max","1080p","720p","480p","360p","audio"], state="readonly", width=12, font=("Segoe UI",10))
        qc.grid(row=0, column=1, sticky=tk.W)
        
        tk.Label(sf, text=self.t('folder'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['text']).grid(row=1, column=0, sticky=tk.W, pady=5, padx=(0,15))
        
        # Закругленная кнопка выбора папки
        fb = tk.Canvas(sf, width=140, height=35, bg=self.c['bg'], highlightthickness=0)
        fb.grid(row=1, column=1, sticky=tk.W)
        fb.create_rounded_rectangle = lambda x1,y1,x2,y2,r=10,**kwargs: fb.create_polygon(
            [x1+r,y1, x1+r,y1, x2-r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y1+r, x2,y2-r, x2,y2-r, x2,y2,
             x2-r,y2, x2-r,y2, x1+r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y2-r, x1,y1+r, x1,y1+r, x1,y1],
            smooth=True, **kwargs)
        fb.create_rounded_rectangle(0, 0, 140, 35, r=10, fill=self.c['accent'], outline='')
        fb.create_text(70, 17.5, text=self.t('choose'), fill='white', font=("Segoe UI",9))
        fb.bind('<Button-1>', lambda e: self.choose())
        fb.bind('<Enter>', lambda e: fb.itemconfig(1, fill=self.c['hover']))
        fb.bind('<Leave>', lambda e: fb.itemconfig(1, fill=self.c['accent']))
        fb.config(cursor='hand2')
        
        self.pl = tk.Label(sf, text=os.path.basename(self.path), font=("Segoe UI",8), bg=self.c['bg'], fg=self.c['text2'])
        self.pl.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(5,0))
        
        # Download
        db_canvas = tk.Canvas(self.root, width=280, height=50, bg=self.c['bg'], highlightthickness=0)
        db_canvas.pack(pady=20)
        db_canvas.create_rounded_rectangle = lambda x1,y1,x2,y2,r=15,**kwargs: db_canvas.create_polygon(
            [x1+r,y1, x1+r,y1, x2-r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y1+r, x2,y2-r, x2,y2-r, x2,y2,
             x2-r,y2, x2-r,y2, x1+r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y2-r, x1,y1+r, x1,y1+r, x1,y1],
            smooth=True, **kwargs)
        self.db_rect = db_canvas.create_rounded_rectangle(0, 0, 280, 50, r=15, fill=self.c['accent'], outline='')
        self.db_text = db_canvas.create_text(140, 25, text=self.t('download'), fill='white', font=("Segoe UI",12,"bold"))
        db_canvas.bind('<Button-1>', lambda e: self.download())
        db_canvas.bind('<Enter>', lambda e: db_canvas.itemconfig(self.db_rect, fill=self.c['hover']))
        db_canvas.bind('<Leave>', lambda e: db_canvas.itemconfig(self.db_rect, fill=self.c['accent']))
        db_canvas.config(cursor='hand2')
        self.db = db_canvas
        
        # Progress
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TCombobox', 
                   fieldbackground=self.c['bg2'], 
                   background=self.c['bg2'],
                   foreground=self.c['text'],
                   selectbackground=self.c['accent'],
                   selectforeground='white',
                   arrowcolor=self.c['accent'],
                   borderwidth=0,
                   relief='flat')
        s.map('TCombobox', 
             fieldbackground=[('readonly', self.c['bg2'])],
             selectbackground=[('readonly', self.c['bg2'])],
             foreground=[('readonly', self.c['text'])])
        s.configure("P.Horizontal.TProgressbar", 
                   background=self.c['accent'], 
                   troughcolor=self.c['bg2'], 
                   borderwidth=0, 
                   thickness=10,
                   troughrelief='flat',
                   relief='flat')
        
        self.pb = ttk.Progressbar(self.root, mode='indeterminate', length=640, style="P.Horizontal.TProgressbar")
        self.pb.pack(pady=10, padx=30)
        
        # Status
        self.st = tk.Label(self.root, text=self.t('ready'), font=("Segoe UI",10), bg=self.c['bg'], fg=self.c['ok'])
        self.st.pack(pady=10)
    
    def show_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0, bg=self.c['bg2'], fg=self.c['text'],
                      activebackground=self.c['accent'], activeforeground='white', borderwidth=0)
        menu.add_command(label="Paste", command=self.paste)
        menu.add_command(label="Clear", command=lambda: self.url.delete(0, tk.END))
        menu.post(event.x_root, event.y_root)
    
    def paste(self):
        try:
            self.url.delete(0, tk.END)
            self.url.insert(0, self.root.clipboard_get())
            self.url.icursor(tk.END)
        except:
            pass
        return "break"
    
    def choose(self):
        f = filedialog.askdirectory(initialdir=self.path)
        if f: 
            self.path = f
            self.pl.config(text=os.path.basename(f))
            self.save_config()
    
    def download(self):
        url = self.url.get().strip()
        # Проверяем что это не placeholder
        if not url or url == self.url_placeholder:
            messagebox.showwarning("Error", "Enter URL")
            return
        if not yt_dlp:
            messagebox.showerror("Error", "yt-dlp not installed")
            return
        threading.Thread(target=self.dl, args=(url,), daemon=True).start()
    
    def dl(self, url):
        self.db.unbind('<Button-1>')
        self.db.config(cursor='')
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
                   'quiet': True, 'no_warnings': True, 'ignoreerrors': False}
            
            # Дополнительные опции для Twitter/X
            if 'twitter.com' in url or 'x.com' in url:
                opts['extractor_args'] = {'twitter': {'api': ['syndication', 'graphql']}}
            
            if self.ffmpeg: opts['merge_output_format'] = 'mp4'
            with yt_dlp.YoutubeDL(opts) as ydl: ydl.download([url])
            self.upd(self.t('complete'), self.c['ok'])
            messagebox.showinfo("Success", f"Saved to:\n{self.path}")
        except Exception as e:
            error_msg = str(e)
            self.upd(self.t('failed'), self.c['err'])
            
            # Более понятные сообщения об ошибках
            if 'No video' in error_msg or 'no video' in error_msg.lower():
                messagebox.showerror("Error", "No video found in this link.\nMake sure the tweet/post contains a video.")
            elif 'Private video' in error_msg or 'private' in error_msg.lower():
                messagebox.showerror("Error", "This video is private or requires authentication.")
            elif 'not available' in error_msg.lower():
                messagebox.showerror("Error", "Video is not available or has been deleted.")
            else:
                messagebox.showerror("Error", f"Download failed:\n{error_msg[:200]}")
        finally:
            self.pb.stop()
            self.db.bind('<Button-1>', lambda e: self.download())
            self.db.config(cursor='hand2')
    
    def ph(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '').strip()
            if percent:
                self.upd(f"{self.t('downloading')}: {percent}", self.c['accent'])
    
    def upd(self, txt, col): self.st.config(text=txt, foreground=col)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
