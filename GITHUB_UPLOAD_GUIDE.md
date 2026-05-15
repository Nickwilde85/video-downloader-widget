# Как загрузить проект на GitHub

## 📋 Подготовка

Все файлы готовы! Проект включает:
- ✅ README.md - главная документация
- ✅ LICENSE - MIT лицензия
- ✅ .gitignore - игнорируемые файлы
- ✅ CONTRIBUTING.md - гайд для контрибьюторов
- ✅ SUPPORTED_SITES.md - список сайтов
- ✅ requirements.txt - зависимости
- ✅ Все исходники

## 🚀 Шаг 1: Создать репозиторий на GitHub

1. Откройте https://github.com/new
2. Заполните:
   - **Repository name**: `video-downloader-widget`
   - **Description**: `Modern Windows widget for downloading videos from 1000+ sites`
   - **Public** (чтобы другие могли использовать)
   - ❌ НЕ добавляйте README, .gitignore, LICENSE (у нас уже есть)
3. Нажмите **Create repository**

## 💻 Шаг 2: Загрузить код

### Вариант A: Через командную строку (рекомендуется)

```bash
# 1. Инициализировать git
git init

# 2. Добавить все файлы
git add .

# 3. Первый commit
git commit -m "Initial commit: Video Downloader Widget v1.0"

# 4. Добавить remote (замените YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/video-downloader-widget.git

# 5. Загрузить на GitHub
git branch -M main
git push -u origin main
```

### Вариант B: Через GitHub Desktop

1. Откройте GitHub Desktop
2. File → Add Local Repository
3. Выберите папку проекта
4. Publish repository
5. Выберите имя и описание
6. Нажмите Publish

### Вариант C: Через веб-интерфейс

1. На странице нового репозитория нажмите "uploading an existing file"
2. Перетащите все файлы (кроме .git, __pycache__, dist, build)
3. Напишите commit message: "Initial commit"
4. Нажмите "Commit changes"

## 📦 Шаг 3: Создать Release с EXE

1. **Соберите EXE**:
   ```bash
   build_exe.bat
   ```

2. **Перейдите в Releases**:
   - На странице репозитория → Releases → Create a new release

3. **Заполните**:
   - **Tag**: `v1.0.0`
   - **Title**: `Video Downloader Widget v1.0.0`
   - **Description**:
     ```markdown
     ## 🎉 Первый релиз!
     
     ### ✨ Возможности
     - Скачивание с 1000+ сайтов
     - 4 темы оформления
     - 2 языка (EN/RU)
     - Выбор качества
     
     ### 📥 Установка
     1. Скачайте VideoDownloader.exe
     2. Запустите
     3. Готово!
     
     ### ⚙️ Опционально
     Для максимального качества установите FFmpeg:
     \`\`\`bash
     winget install Gyan.FFmpeg
     \`\`\`
     ```

4. **Прикрепите файлы**:
   - Перетащите `dist/VideoDownloader.exe`
   - Можно добавить `requirements.txt`

5. **Publish release**

## 🎨 Шаг 4: Добавить скриншоты (опционально)

1. Создайте папку `screenshots/` в репозитории
2. Сделайте скриншоты приложения:
   - Pink theme
   - Blue theme
   - Green theme
   - Purple theme
3. Загрузите в папку
4. Обновите README.md с реальными ссылками на скриншоты

## 📝 Шаг 5: Настроить репозиторий

### Topics (теги)
На странице репозитория → About → Settings → Topics:
- `video-downloader`
- `youtube-downloader`
- `tiktok-downloader`
- `python`
- `tkinter`
- `windows`
- `yt-dlp`
- `gui`
- `widget`

### Description
```
Modern Windows widget for downloading videos from YouTube, TikTok, Instagram, Twitter and 1000+ sites
```

### Website
Если есть - добавьте ссылку

## 🔧 Шаг 6: Настроить GitHub Pages (опционально)

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: main, folder: / (root)
4. Save

Теперь README будет доступен как веб-страница!

## 📢 Шаг 7: Продвижение

### Поделиться:
- Reddit: r/Python, r/software
- Twitter/X: с хештегами #Python #VideoDownloader
- Dev.to: написать статью
- Hacker News
- Product Hunt

### Добавить badges в README:
```markdown
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/video-downloader-widget)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/video-downloader-widget)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/video-downloader-widget)
```

## 🔄 Обновления

Когда добавите новые функции:

```bash
# 1. Внести изменения в код
# 2. Commit
git add .
git commit -m "Add: описание изменений"

# 3. Push
git push

# 4. Создать новый Release
# GitHub → Releases → New release
# Tag: v1.1.0
# Прикрепить новый EXE
```

## ✅ Чеклист перед публикацией

- [ ] Все файлы добавлены
- [ ] README.md заполнен
- [ ] LICENSE добавлен
- [ ] .gitignore настроен
- [ ] EXE собран и протестирован
- [ ] Скриншоты добавлены
- [ ] Release создан
- [ ] Topics добавлены
- [ ] Description заполнен

## 🎉 Готово!

Ваш проект на GitHub:
```
https://github.com/YOUR_USERNAME/video-downloader-widget
```

Теперь другие могут:
- ⭐ Ставить звезды
- 🍴 Делать форки
- 📥 Скачивать EXE
- 🐛 Сообщать о багах
- 🤝 Вносить вклад

## 💡 Советы

1. **Отвечайте на Issues** - это привлекает пользователей
2. **Обновляйте регулярно** - показывает что проект живой
3. **Добавьте CHANGELOG.md** - история изменений
4. **Используйте Projects** - для планирования
5. **Добавьте CI/CD** - автоматическая сборка

## 📚 Полезные ссылки

- [GitHub Docs](https://docs.github.com)
- [Markdown Guide](https://www.markdownguide.org)
- [Shields.io](https://shields.io) - badges
- [Choose a License](https://choosealicense.com)

Удачи с проектом! 🚀
