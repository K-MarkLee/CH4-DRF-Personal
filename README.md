# CH4-DRF-Personal
# Django-DRF Personal Work

## 개요 
이 프로젝트는 스파르타 마켓의 DRF 구현으로 사용자가 자신의 프로필과 상품 정보를 관리 할 수 있는 RESTful API를 제공한다.  주요 기능은 아래와 같다.

  
1. 로그인 관리 : 회원가입, 로그인 을 할 수 있는 기능 제공.
2. 프로필 관리 : 로그인한 사용자가 자시느이 정보를 조회하는 기능 제공.
3. JWT 기반 인증 기능 제공.

&nbsp;
## 설치 및 실행

1. 프로젝트 클론
    - ` git clone <repo - url>`
    - ` cd <project-directory>` 

&nbsp;   

2. 가상환경 설정 및 활성화
    - `python -m venv venv`
    - `source venv/Scripts/activate`

&nbsp;

3. 패키지 설치
    - `pip install -r requirements.txt`

&nbsp;

4. 데이터베이스 마이그레이션
    - `python manage.py makemigrations`
    - `python manage.py migrate`

&nbsp;

5. 서버 실행
    - `python manage.py runserver`


---
## 기능 테스트

### 1. 회원가입
![회원가입](./images/create_account.png)


### 1.1. 회원가입 검증
![회원가입 검증](./images/email_username_error_create.png)

### 1.2 회원가입 검증2
![회원가입 검증2](./images/password_error_create.png)


### 1.3 회원가입 검증3
![회원가입 검증3](./images/birth_date_error_create.png)


&nbsp;

### 2. 로그인
![로그인](./images/login_account.png)

### 2.2 로그인 검증
![로그인 검증](./images/invalid_error_login.png)


&nbsp;

### 3. 로그 아웃
![로그아웃](./images/log_out.png)


&nbsp;


### 4. 상품 등록
![상품등록](./images/product_create.png)

### 4.1 상품 등록 검증
![상품등록 검증](./images/not_filled_form_product_create.png)


&nbsp;

### 5. 상품 조회
![상품조회](./images/product_list.png)

### 5.1 상품 조회 (페이지네이션)
![페이지네이션](./images/pagination_product_list.png)


&nbsp;


### 6. 상품 수정
![상품수정](./images/product_update.png)

### 6.1 상품 수정 검증
![상품수정 검증](./images/no_access_error_product_update.png)


&nbsp;

### 7. 상품 제거
![상품제거](./images/product_delete.png)

### 7.1 상품 제거 검증
![상품제거 검증](./images/no_access_error_product_delete.png)

### 7.2 상품 제거 후 리스트
![제거 후 리스트](./images/product_list_after_product_delete.png)


&nbsp;


### 8. 프로필
![프로필](./images/profile.png)

### 8.1 프로필 검증
![프로필 검증](./images/login_access_error_profile.png)

---
&nbsp;

## 트러블 슈팅

### 1. JWT 토큰 관련
- 문제 : Access Token 은 입력을 받는데 반에, Refrsh Token 을 받지 않음
- 해결 : settings 에서 토큰 라이브러리 등록

&nbsp;

### 2. 
