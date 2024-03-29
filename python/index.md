# Python

### [Chapter 01. 기본 설정](chapter_01/index.md)
- 01-1. Python 소개
- 01-2. Python 설치
- 01-3. Editor 설치
- 01-4. Linux 소개 및 Linux 기본 명령어
- 01-5. Houdini 설치 및 Environments
- 01-6. Python 둘러보기
    - Python 으로 무엇을 할 수 있을까 ?

### Chapter 02. Start Python Programming
- 02-1. Hello World!
- 02-2. 자료형
- 02-3. 컴퓨터가 데이터를 표현하는 방식
- 02-4. 변수와 연산자
- 02-5. 비트 연산자 및 비트 연산 (2진수, 8진수, 10진수, 16진수)
- 02-6. Index, Slice

### Chapter 03. 반복문
- 03-1. while에 의한 문장의 반복
- 03-2. for문에 의한 문장의 반복
- 문제 풀이

### Chapter 04. 분기문
- 04-1. 조건적 실행과 흐름의 분기
- 04-2. 반복문의 생략과 탈출: continue & break
- 주석이 있어야 비소로 완성된 프로그램

### Chapter 05. 내장 함수
- 05-1. 문자열 내장 함수
- 05-2. 리스트, 튜플 내장 함수
- 05-3. 딕셔너리 내장 함수
- 05-4. map, zip, filter, ...

### [Chapter 06. 함수](chapter_06/index.md)
- 06-1. 함수 정의
- 06-2. 변수의 존재 기간과 접근범위 1: 지역변수
- 06-3. 변수의 존재 기간과 접근범위 2: 전역변수
- 06-4. 재귀함수에 대한 이해
- 06-5. lambda 함수
- 06-6. 매개변수와 디폴트 값(default value)
- 06-7. 코딩 스타일
- 문제 풀이

### Chapter 07. 파일 입출력
- 07-1. open: 파일 읽고 쓰기
- 07-2. json 형식의 파일 읽고 쓰기
- 07-3. 프로그램의 입출력: argv
- 07-4. 예외 처리 (try~except)
- 문제 풀이

### [Chapter 08. Class](chapter_08/index.md)
- 08-1. 이름 공간(namespace)에 대한 소개
- 08-2. 클래스의 기본 구조
- 08-3. 생성자(Constructor)와 소멸자(Destructor)
- 08-4. 클래스(class)와 객체(object)
- 08-5. self의 의미
- 08-6. __slots__이란?
- 문제 풀이

### [Chapter 09. 보다 견고한 클래스](chapter_09/index.md)
- 09-1. 비공개 속성 (_, __)
- 09-2. 정보은닉(Information Hiding) & 캡슐화(Encapsulation)
- 문제 풀이

### [Chapter 10. 상속(Inheritance)과 다형성(Polymorphism)](chapter_10/index.md)
- 10-1. 정적 메서드(staticmethod) & 클래스 메서드(classmethod)
- 10-2. 상속(is) 혹은 포함(has) 관계
- 10-3. 메서드 오버라이드(override)
- 10-4. 추상 클래스
- 10-5. 다중 상속
- 10-6. 죽음의 다이아몬드(the Deadly Diamond of Death: DDD) 란?
- 10-7. 객체 지향 프로그래밍
- 문제 풀이

### [Chapter 11. 이터레이터(iterator)](chapter_11/index.md)
- 11-1. 반복 가능 객체란
- 11-2. 이터레이터 생성
- 11-3. iter, next 함수 활용
- 문제 풀이

### [Chapter 12. 제네레이터(generator)](chapter_12/index.md)
- 12-1. yield 키워드에 대하여
- 12-2. 제네레이터 생성
- 12-3. yield from 키워드로 외부에 데이터 전달
- 12-4. 유용한 모듈 (itertools)
- 문제 풀이

### [Chapter 13. 동시성(concurrency)과 병렬성(parallelism)](chapter_13/index.md)
- 13-1. Python GIL(Global Interpreter Lock)
- 13-2. 프로세스(process)
- 13-3. 스레드(thread)
- 13-4. 코루틴(coroutine)
- 13-5. 동시성 관리 구현에 유용한 모듈 (futures, asyncio)
- 13-6. 태스크(task)
- 13-7. asyncpg (asyncio 기반의 PostgreSQL 라이브러리)
- 13-8. aioredis (asyncio 기반의 Redis 라이브러리)
- 문제 풀이

### [Chapter 14. 장식자(Decorator)](chapter_14/index.md)
- 14-1. 데코레이터 생성
- 14-2. 매개변수와 반환값이 존재하는 데코레이터
- 14-3. 클래스 기반의 데코레이터
- 문제 풀이

### [Chapter 15. 유용한 모듈](chapter_15/index.md)
- 15-1. 정규표현식(re)
- 15-2. 이진 탐색 트리(bisect)
- 15-3. 이미지(Pillow)
- 15-4. Json형식(JmesPath)
- 15-5. heap 자료구조(heapq)
- 15-6. 자료구조 모음(collections)
- 15-7. TUI기반의 옵션처리(Typer)
- 15-8. Database ORM(SQLAlchemy)

### Chapter 16. 모듈과 패키지
- 16-1. 모듈 생성
- 16-2. 모듈과 시작점
- 16-3. 하위 패키지 구성
- 16-4. 패키지 사용
- 문제 풀이

### [Chapter 17. GUI 프로그래밍](chapter_17/index.md)
- 17-1. PySide6 소개 및 설치
- 17-2. 앱 만들기
- 17-3. Signal & Slot
- 17-4. Qwidgets (QLabel, QCheckBox, QComboBox, ...)
- 17-5. 레이아웃 (QVBoxLayout, QHBoxLayout, ...)
- 17-6. 액션, 툴바, 메뉴
- 17-7. 대화 상자 (QMessageBox, ...)
- 17-8. 윈도우 간 시그널 연결
- 17-9. 이벤트 (마우스 이벤트, 컨텍스트 메뉴, 이벤트 계층 구조)
- 17-10. 계산기 앱 제작

### Chapter 18. Qt 디자이너
- 18-1. Qt 디자이너 설치 (Linux)
- 18-2. 파이썬에 .ui 파일 로딩
- 18-3. 파이썬 코드로 .ui 파일 변환
- 18-4. 애플레케이션 빌드

### Chapter 19. Theme
- 19-1. 다크 모드
- 19-2. 아이콘 파일
- 19-3. Qt 스타일시트(QSS)

### [Chapter 20. 모델 뷰 아키텍처](chapter_20/index.md)
- 20-1. MVC (Model-View-Contoller)
- 20-2. QListView, QTableView, QTreeView
- 20-3. Qt 모델에서 SQL 데이터베이스 쿼리
- 20-4. ToDo List 제작

### [Chapter 21. 동시 실행](chapter_21/index.md)
- 21-1. QThread
- 21-2. Slot Decorator
- 21-3. 스레드 풀 (Qrunnable, QThreadPool, ...)

### Chapter 22. PySide 심화
- 22-1. 타이머 (인터벌, 싱글샷, 딜레이, ...)
- 22-2. 확장 시그널 (사용자 정의)
- 22-3. 시스템 트레이

### Chapter 23. PyInstaller 패키징
- 23-1. 요구 사항 및 시작 방법
- 23-2. 기본 앱 작성 및 .spec 파일

### Chapter 24. Linux 패키지 작성
- 24-1. 빌드 체크 및 패키지 구조화
- 24-2. .desktop 파일
- 24-3. 패키지 작성 및 설치
- 24-4. 빌드 스크립트

### [Chapter 25. 데이터베이스(Database)](chapter_25/index.md)
- 25-1. 데이터베이스 개론
- 25-2. 테이블 설계 및 구현 (Database Schema)
- 25-3. SQL 기초 (SELECT, CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, ...)
- 25-4. JOIN (INNER, OUTER, CROSS, SELF)
- 25-5. 내장 함수
- 25-6. 트랜잭션
- 25-7. TRIGGER
- 25-8. EVENT (Scheduler)
- 25-9. PROCEDURE & FUNCTION
- 25-10. 계정 생성/삭제 및 권한 부여/취소 (CREATE USER, DROP USER, GRANT, REVOKE)
- 25-11. Docker를 이용한 MySQL 설치

### Chapter 26. 데이터 모델링
- 26-1. 개체, 관계, 속성의 이해
- 26-2. 업무 관리 ERD 예제 뜯어보기
- 26-3. 정규화(Normalize)

### Chapter 27. 데이터베이스 API
- 27-1. Python의 데이터베이스 모듈
- 27-2. Web Server와 Database Server 그리고 Python 연동

### [Chapter 28. Back-end](chapter_28/index.md)
- 28-1. 백엔드(back-end)에 대하여
- 28-2. Web Framework 소개
- 28-3. HTTP
- 28-4. API 엔드포인트 아키텍처 패턴
- 28-5. Flask를 이용한 API 작성
- 28-6. FastAPI를 이용한 API 작성
- 28-7. API 개발을 위한 유용한 툴

### [Chapter 29. Algorithm](chapter_29/index.md)
- 29-1. 알고리즘 개요
- 29-2. 빅오(Big-O 표기법)
- 29-3. 연결 리스트(Linked List)
- 29-4. 이중 연결 리스트
- 29-5. 스택(Stack) & 큐(Queue)
- 29-6. 트리(Tree)
- 29-7. Selection/Insertion 정렬 알고리즘
- 29-8. Bubble/Shell 정렬 알고리즘
- 29-9. Quick/Radix 정렬 알고리즘
- 29-10. Merge/Heap 정렬 알고리즘
- 29-11. 이진 검색 알고리즘
- 문제 풀이

### [Chapter 30. Design Pattern](chapter_30/index.md)
- 30-1. 디자인 패턴 개요
- 30-2. Singleton Pattern
- 30-3. Factory Pattern
- 30-4. Observer Pattern

### [Chapter 31. 테스트 주도 개발(Test Driven Development, TDD)](chapter_31/index.md)
- 31-1. TDD 개요
- 31-2. Python에서의 TDD
