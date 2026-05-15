# Video Downloader Widget

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Downloads](https://img.shields.io/badge/Sites-1000+-orange.svg)

**Современный виджет для скачивания видео с 1000+ сайтов**

[Скачать](#установка) • [Возможности](#возможности) • [Поддерживаемые сайты](SUPPORTED_SITES.md) • [Документация](#использование)

</div>

---

## 🎯 Поддерживаемые платформы

### ✅ Основные (работают отлично)
- **YouTube** - все форматы, 4K/8K, плейлисты
- **TikTok** - видео без водяных знаков
- **Instagram** - посты, reels, stories
- **Facebook** - публичные видео
- **Twitter/X** - публичные видео
- **Pinterest** - видео пины
- **Vimeo** - все форматы
- **Reddit** - v.redd.it видео
- **Dailymotion** - все видео

### 🌍 Региональные
- VK (ВКонтакте), Rutube, OK.ru, Bilibili, NicoNico

### 📺 И ещё 1000+ сайтов!

Полный список: [SUPPORTED_SITES.md](SUPPORTED_SITES.md)

## ✨ Возможности

- 🎨 **4 темы оформления** (Purple, Blue, Green, Pink)
- 🌍 **2 языка** (English, Русский)
- 📁 **Запоминает папку** для сохранения
- 🎬 **Выбор качества** (max, 1080p, 720p, 480p, 360p, audio)
- 🚀 **Без консоли** - чистый интерфейс
- 💾 **Сохранение настроек** между запусками
- 🎯 **Закругленные элементы** - современный дизайн
- ⚡ **Быстрая работа** - многопоточная загрузка

## 📥 Установка

### Вариант 1: Готовый EXE (Рекомендуется)

1. Скачайте `VideoDownloader.exe` из [Releases](../../releases)
2. Запустите - всё работает сразу!
3. (Опционально) Установите FFmpeg для максимального качества:
   ```bash
   winget install Gyan.FFmpeg
   ```

### Вариант 2: Из исходников

```bash
git clone https://github.com/yourusername/video-downloader-widget.git
cd video-downloader-widget
pip install -r requirements.txt
python video_downloader.py
```

### Вариант 3: Собрать EXE самостоятельно

```bash
pip install -r requirements.txt
build_exe.bat
```

## 🚀 Использование

1. **Запустите приложение**
2. **Вставьте ссылку** (ПКМ → Paste или Ctrl+V)
3. **Выберите качество** (max, 1080p, 720p и т.д.)
4. **Нажмите Download**

## 📁 Структура проекта

```
video-downloader-widget/
├── video_downloader.py      # Основной файл
├── requirements.txt          # Зависимости
├── run.bat                   # Запуск без консоли
├── build_exe.bat            # Сборка EXE
├── README.md                 # Документация
├── SUPPORTED_SITES.md       # Список сайтов
└── LICENSE                   # MIT License
```

## ⚙️ Требования

- Windows 10/11
- Python 3.8+ (для исходников)
- FFmpeg (опционально, для макс. качества)

## 🤝 Вклад в проект

Приветствуются любые улучшения! См. [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 Лицензия

MIT License - см. [LICENSE](LICENSE)

## 🙏 Благодарности

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - библиотека для загрузки
- [FFmpeg](https://ffmpeg.org/) - обработка видео

---

<div align="center">

**Сделано с ❤️ для сообщества**

⭐ Поставьте звезду если проект понравился!

</div>
