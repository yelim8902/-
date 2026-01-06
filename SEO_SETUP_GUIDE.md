# SEO 설정 상세 가이드

이 문서는 SEO_STRATEGY.md의 "추가 작업 필요" 항목들을 단계별로 상세히 설명합니다.

---

## 1️⃣ 실제 도메인 URL로 업데이트하기

### 📍 현재 상황
현재 코드에 `your-domain.vercel.app`이라는 플레이스홀더가 여러 곳에 있습니다. 이를 실제 도메인으로 변경해야 합니다.

### 🔍 1단계: Vercel 도메인 확인하기

**방법 1: Vercel 대시보드에서 확인**
1. https://vercel.com 접속 후 로그인
2. 프로젝트 선택
3. **Settings** → **Domains** 메뉴 클릭
4. 표시된 도메인 확인 (예: `roulette-abc123.vercel.app` 또는 커스텀 도메인)

**방법 2: GitHub에서 확인**
1. GitHub 저장소의 **Settings** → **Pages** (또는 Actions 탭)
2. 배포된 URL 확인

**방법 3: 브라우저에서 확인**
- 배포된 사이트를 브라우저에서 열고 주소창의 URL 확인

### ✏️ 2단계: 파일 수정하기

다음 파일들에서 `your-domain.vercel.app`을 실제 도메인으로 변경해야 합니다:

#### 📄 `index.html` 수정 (총 5곳)

**1. Open Graph URL (28번째 줄)**
```html
<!-- 변경 전 -->
<meta property="og:url" content="https://your-domain.vercel.app/" />

<!-- 변경 후 (예시) -->
<meta property="og:url" content="https://roulette-abc123.vercel.app/" />
```

**2. Open Graph 이미지 (39번째 줄)**
```html
<!-- 변경 전 -->
<meta property="og:image" content="https://your-domain.vercel.app/og-image.png" />

<!-- 변경 후 -->
<meta property="og:image" content="https://roulette-abc123.vercel.app/og-image.png" />
```

**3. Twitter URL (48번째 줄)**
```html
<!-- 변경 전 -->
<meta property="twitter:url" content="https://your-domain.vercel.app/" />

<!-- 변경 후 -->
<meta property="twitter:url" content="https://roulette-abc123.vercel.app/" />
```

**4. Twitter 이미지 (59번째 줄)**
```html
<!-- 변경 전 -->
<meta property="twitter:image" content="https://your-domain.vercel.app/og-image.png" />

<!-- 변경 후 -->
<meta property="twitter:image" content="https://roulette-abc123.vercel.app/og-image.png" />
```

**5. Canonical URL (67번째 줄)**
```html
<!-- 변경 전 -->
<link rel="canonical" href="https://your-domain.vercel.app/" />

<!-- 변경 후 -->
<link rel="canonical" href="https://roulette-abc123.vercel.app/" />
```

**6. JSON-LD 구조화된 데이터 (95번째 줄)**
```json
// 변경 전
"url": "https://your-domain.vercel.app/",

// 변경 후
"url": "https://roulette-abc123.vercel.app/",
```

#### 📄 `sitemap.xml` 수정

```xml
<!-- 변경 전 -->
<loc>https://your-domain.vercel.app/</loc>

<!-- 변경 후 -->
<loc>https://roulette-abc123.vercel.app/</loc>
```

#### 📄 `robots.txt` 수정

```txt
<!-- 변경 전 -->
Sitemap: https://your-domain.vercel.app/sitemap.xml

<!-- 변경 후 -->
Sitemap: https://roulette-abc123.vercel.app/sitemap.xml
```

### 💡 팁: 일괄 변경하기

**VS Code에서 일괄 변경:**
1. `Cmd + Shift + F` (Mac) 또는 `Ctrl + Shift + F` (Windows)
2. 검색창에 `your-domain.vercel.app` 입력
3. "Replace" 탭 클릭
4. 실제 도메인 입력 (예: `roulette-abc123.vercel.app`)
5. "Replace All" 클릭

**터미널에서 일괄 변경:**
```bash
# macOS/Linux
sed -i '' 's/your-domain\.vercel\.app/roulette-abc123.vercel.app/g' index.html sitemap.xml robots.txt

# Windows (Git Bash)
sed -i 's/your-domain\.vercel\.app/roulette-abc123.vercel.app/g' index.html sitemap.xml robots.txt
```

### ✅ 확인 방법
변경 후 브라우저에서 페이지 소스 보기 (`Cmd + Option + U` 또는 `Ctrl + U`)로 메타 태그가 올바르게 변경되었는지 확인하세요.

---

## 2️⃣ OG 이미지 생성하기

OG 이미지는 페이스북, 카카오톡, 트위터 등에서 링크를 공유할 때 표시되는 미리보기 이미지입니다.

### 📐 이미지 사양
- **크기**: 1200px × 630px (가로:세로 = 1.91:1)
- **형식**: PNG 또는 JPG
- **파일 크기**: 1MB 이하 권장
- **파일명**: `og-image.png`

### 🎨 디자인 아이디어

**옵션 1: 룰렛 이미지 + 텍스트**
- 배경: 파스텔 톤 또는 그라데이션
- 중앙: 룰렛 원형 이미지 (실제 룰렛 스크린샷 또는 일러스트)
- 상단: "벌칙 룰렛" 큰 글씨
- 하단: "친구들과 함께 재미있게!" 서브 텍스트

**옵션 2: 심플한 텍스트 중심**
- 배경: 밝은 색상 (흰색, 연한 파스텔)
- 중앙: "벌칙 룰렛" 큰 타이틀
- 작은 텍스트: "커플 룰렛 | 19금 룰렛 | 무료"

### 🛠️ 이미지 제작 방법

#### 방법 1: 온라인 도구 사용 (추천 - 초보자용)

**Canva 사용:**
1. https://www.canva.com 접속 (무료 계정 생성)
2. "사용자 지정 크기" 클릭
3. 너비: 1200px, 높이: 630px 입력
4. 디자인 제작
5. 다운로드 → PNG 형식 선택

**Figma 사용:**
1. https://www.figma.com 접속 (무료 계정)
2. 새 파일 생성
3. 프레임 크기: 1200 × 630
4. 디자인 제작
5. Export → PNG 선택

#### 방법 2: Photoshop / GIMP 사용

**Photoshop:**
1. 새 파일 생성 (1200 × 630px)
2. 디자인 제작
3. File → Export → Export As → PNG

**GIMP (무료):**
1. 새 이미지 생성 (1200 × 630px)
2. 디자인 제작
3. File → Export As → `og-image.png`

#### 방법 3: 코드로 생성 (고급)

HTML Canvas를 사용해 동적으로 생성할 수도 있습니다. (선택사항)

### 📁 파일 저장 위치

**Vercel 배포 시:**
- 프로젝트 루트에 `public` 폴더 생성
- `public/og-image.png`로 저장

**폴더 구조:**
```
roulette/
├── index.html
├── public/
│   └── og-image.png  ← 여기에 저장
├── sitemap.xml
└── robots.txt
```

**만약 `public` 폴더가 없다면:**
```bash
mkdir public
# 이미지를 public/og-image.png로 복사
```

### 🔗 이미지 URL 확인

배포 후 다음 URL로 접속해서 이미지가 제대로 보이는지 확인:
```
https://your-domain.vercel.app/og-image.png
```

### ✅ 테스트 방법

**페이스북 공유 디버거:**
1. https://developers.facebook.com/tools/debug/ 접속
2. URL 입력 후 "디버그" 클릭
3. 이미지가 올바르게 표시되는지 확인

**카카오톡 링크 미리보기:**
1. 카카오톡에서 링크 공유
2. 미리보기 이미지 확인

---

## 3️⃣ Favicon 추가하기

Favicon은 브라우저 탭에 표시되는 작은 아이콘입니다.

### 📐 이미지 사양
- **크기**: 32×32px 또는 16×16px (32×32px 권장)
- **형식**: PNG, ICO, 또는 SVG
- **파일명**: `favicon.png` 또는 `favicon.ico`

### 🎨 디자인 아이디어

**옵션 1: 룰렛 원형 아이콘**
- 원형 배경에 화살표 또는 룰렛 패턴

**옵션 2: 텍스트 아이콘**
- "벌" 또는 "룰" 한 글자
- 또는 "BR" (벌칙 룰렛 이니셜)

**옵션 3: 심플한 기호**
- 원형 + 화살표
- 또는 룰렛 휠 모양

### 🛠️ Favicon 제작 방법

#### 방법 1: 온라인 Favicon 생성기 (가장 쉬움)

**Favicon.io:**
1. https://favicon.io 접속
2. "Text" 또는 "Image" 선택
3. 텍스트 입력 (예: "벌") 또는 이미지 업로드
4. 배경색, 폰트 선택
5. "Create Favicon" 클릭
6. 다운로드 → `favicon.png`로 저장

**RealFaviconGenerator:**
1. https://realfavicongenerator.net 접속
2. 이미지 업로드 (최소 260×260px 권장)
3. 각 플랫폼별 미리보기 확인
4. "Generate your Favicons and HTML code" 클릭
5. 다운로드

#### 방법 2: 이미지 편집 프로그램 사용

**Photoshop / GIMP:**
1. 새 파일 생성 (32×32px)
2. 디자인 제작
3. PNG로 저장

**Figma:**
1. 32×32px 프레임 생성
2. 디자인 제작
3. Export → PNG

#### 방법 3: 기존 이미지 리사이즈

이미 룰렛 관련 이미지가 있다면:
1. 온라인 리사이즈 도구 사용 (예: https://www.iloveimg.com/resize-image)
2. 32×32px로 리사이즈
3. 다운로드

### 📁 파일 저장 위치

**Vercel 배포 시:**
- 프로젝트 루트에 `public` 폴더 생성
- `public/favicon.png`로 저장

**폴더 구조:**
```
roulette/
├── index.html
├── public/
│   ├── og-image.png
│   └── favicon.png  ← 여기에 저장
├── sitemap.xml
└── robots.txt
```

### ✅ 코드 확인

`index.html`의 63번째 줄에 이미 favicon 링크가 있습니다:
```html
<link rel="icon" type="image/png" href="/favicon.png" />
```

이 코드는 `public/favicon.png` 파일을 자동으로 찾습니다.

### 🔍 테스트 방법

1. 브라우저에서 사이트 접속
2. 브라우저 탭 확인 (favicon이 표시되는지)
3. 만약 보이지 않으면:
   - 브라우저 캐시 삭제 (`Cmd + Shift + R` 또는 `Ctrl + Shift + R`)
   - 또는 시크릿 모드에서 확인

---

## 🚀 전체 작업 순서 요약

1. **Vercel 도메인 확인**
   - Vercel 대시보드에서 실제 도메인 확인

2. **도메인 URL 일괄 변경**
   - `index.html` (5곳)
   - `sitemap.xml` (1곳)
   - `robots.txt` (1곳)

3. **OG 이미지 제작**
   - Canva 또는 Figma로 1200×630px 이미지 제작
   - `public/og-image.png`로 저장

4. **Favicon 제작**
   - Favicon.io로 32×32px 아이콘 제작
   - `public/favicon.png`로 저장

5. **Git 커밋 & 푸시**
   ```bash
   git add .
   git commit -m "SEO: 도메인 URL 업데이트 및 이미지 추가"
   git push
   ```

6. **배포 확인**
   - Vercel 자동 배포 대기 (1-2분)
   - 브라우저에서 확인
   - 페이스북 공유 디버거로 OG 이미지 테스트

---

## ❓ 자주 묻는 질문 (FAQ)

**Q: `public` 폴더가 없는데 어떻게 하나요?**
A: 프로젝트 루트에 `public` 폴더를 직접 생성하세요:
```bash
mkdir public
```

**Q: 이미지를 만들 줄 모르는데 어떻게 하나요?**
A: Canva나 Favicon.io 같은 온라인 도구를 사용하면 디자인 지식 없이도 쉽게 만들 수 있습니다.

**Q: 커스텀 도메인을 사용하고 있는데요?**
A: 커스텀 도메인(예: `penalty-roulette.com`)을 사용한다면, 모든 `your-domain.vercel.app`을 커스텀 도메인으로 변경하세요.

**Q: 이미지를 만들었는데 배포 후 안 보여요.**
A: 
1. 파일이 `public` 폴더에 있는지 확인
2. 파일명이 정확한지 확인 (`og-image.png`, `favicon.png`)
3. 브라우저 캐시 삭제 후 다시 확인
4. Vercel 배포 로그 확인

**Q: OG 이미지가 페이스북에서 안 바뀌어요.**
A: 페이스북은 캐시를 사용합니다. https://developers.facebook.com/tools/debug/ 에서 URL을 입력하고 "스크래핑 새로고침" 버튼을 클릭하세요.

---

## 📞 도움이 필요하신가요?

각 단계에서 막히는 부분이 있으면 언제든지 물어보세요! 🚀

