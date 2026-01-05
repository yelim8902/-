# 벌칙 룰렛 웹사이트

## 파일 구조

- **index.html**: 기본 버전 - 고정된 벌칙들만 있는 룰렛
- **custom.html**: 커스텀 버전 - 사용자가 직접 벌칙을 추가/삭제할 수 있는 룰렛

## 사용 방법

브라우저에서 `index.html` 또는 `custom.html` 파일을 열면 됩니다.

## React + CSS vs HTML만 사용의 차이

### HTML + CSS + Vanilla JavaScript (현재 방식)

**장점:**
- ✅ **간단함**: 별도의 빌드 도구나 설정이 필요 없음
- ✅ **빠른 시작**: 파일 하나만 열면 바로 작동
- ✅ **가벼움**: 추가 라이브러리 없이 순수 웹 기술만 사용
- ✅ **이해하기 쉬움**: 코드가 한 곳에 모여있어 학습에 좋음
- ✅ **배포 간단**: 파일을 서버에 올리기만 하면 됨

**단점:**
- ❌ **코드 재사용**: 컴포넌트를 재사용하기 어려움
- ❌ **상태 관리**: 복잡한 상태 관리가 어려움
- ❌ **확장성**: 프로젝트가 커지면 관리가 어려워짐
- ❌ **개발 도구**: 자동완성, 타입 체크 등이 제한적

**언제 사용?**
- 작은 프로젝트
- 빠른 프로토타이핑
- 학습 목적
- 단일 페이지 애플리케이션

### React + CSS

**장점:**
- ✅ **컴포넌트 재사용**: 룰렛, 버튼 등을 컴포넌트로 만들어 재사용 가능
- ✅ **상태 관리**: 복잡한 상태를 체계적으로 관리 (useState, Context API 등)
- ✅ **생태계**: 많은 라이브러리와 도구 사용 가능
- ✅ **개발 경험**: Hot Reload, TypeScript, 개발 도구 등
- ✅ **확장성**: 큰 프로젝트도 체계적으로 관리 가능
- ✅ **성능 최적화**: Virtual DOM, 메모이제이션 등

**단점:**
- ❌ **복잡도**: 초기 설정과 학습 곡선이 있음
- ❌ **빌드 과정**: Webpack, Vite 등 빌드 도구 필요
- ❌ **파일 크기**: React 라이브러리 자체가 추가됨
- ❌ **설정**: 개발 환경 설정이 필요함

**언제 사용?**
- 큰 프로젝트
- 여러 페이지가 있는 웹앱
- 팀 프로젝트
- 재사용 가능한 컴포넌트가 많은 경우
- 복잡한 상태 관리가 필요한 경우

## 예시 비교

### HTML 방식 (현재)
```html
<!-- 모든 것이 한 파일에 -->
<script>
  let penalties = ['물 한 잔', '딱밤'];
  function addPenalty() { ... }
</script>
```

### React 방식
```jsx
// Roulette.jsx
function Roulette({ penalties, onSpin }) {
  return <canvas>...</canvas>;
}

// PenaltyList.jsx
function PenaltyList({ penalties, onDelete }) {
  return <div>...</div>;
}

// App.jsx
function App() {
  const [penalties, setPenalties] = useState(['물 한 잔', '딱밤']);
  return (
    <Roulette penalties={penalties} />
    <PenaltyList penalties={penalties} />
  );
}
```

## 결론

**현재 프로젝트(벌칙 룰렛)의 경우:**
- HTML 방식이 적합합니다! 
- 단순한 기능, 빠른 실행, 학습 목적에 완벽합니다.

**React를 사용한다면:**
- 여러 게임 모드가 있거나
- 사용자 계정/저장 기능이 있거나
- 여러 페이지가 필요한 경우에 유용합니다.

