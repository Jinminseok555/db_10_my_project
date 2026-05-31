# 🥗 자취생 냉장고 식재료 매니저 (Fresh Jachi Fridge)

대학생 자취생들을 위한 스마트 식재료 유통기한 관리 및 레시피 추천 시스템입니다. 
냉장고에 있는 재료를 효율적으로 관리하고, 유통기한 임박 재료를 활용한 최적의 레시피를 추천받아 식비 절감과 건강한 식생활을 돕습니다.

---

## 🛠️ 주요 기능
- **냉장고 재료 관리**: 식재료 추가, 수량 수정, 유통기한 관리
- **레시피 탐색**: 조리 시간, 난이도별 맞춤 레시피 조회
- **해먹기 매칭**: 현재 냉장고 재료로 즉시 만들 수 있는 요리 추천
- **상황별 모드**: 시험기간(간편식), 종강(요리) 등 상황에 따른 추천 알고리즘

---

## 🏗️ 설치 및 실행 방법

### 1. uv 환경 설정 (최초 1회)
```bash
# Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"