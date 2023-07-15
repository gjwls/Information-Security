# Ch 1. Network Basics

## Terms of Network

네트워크는 전송매체를 매개로 서로 연결되어 데이터를 교환하는 시스템의 모음

System은 내부 규칙에 따라 능동적으로 동작하는 대상임과 동시에 논리적인 대상들을 뜻함

Interface는 시스템과 시스템을 연결하기 위한 표준화된 접근 방법

Transmission Media는 시스템끼리 정해진 인터페이스를 연동해 데이터를 전달하기 위한 물리적인 전송 수단

Protocol은 전송 매체를 통해 데이터를 교환하는 표준화된 특정 규칙

Network는 통신 매체를 공유할 때 사용하는 하나의 단위

Internet은 모든 네트워크가 유기적으로 연결되어 동작하는 통합 네트워크

Standardization은 서로 다른 시스템이 상호 연동해 동작하기 위한 방식

Node는 인터넷에 연결된 시스템 단위

Host는 컴퓨팅 기능이 있는 시스템 단위

Client는 서비스를 이용하는 시스템

Server는 서비스를 제공하는 시스템

## Function of Network

1. Physical Layer
   - 전송매체로 연결
   - 인터페이스 규칙과 전송 매체의 특성을 다룸
2. Data Link Layer
   - 송수신 호스트가 오류를 인지할 수 있도록 함
3. Network Layer
   - 데이터가 올바른 경로를 선택할 수 있도록 지원
   - 혼잡 제어의 기능도 수행
4. Transport Layer
   - 송신 프로세스와 수신 프로세스 간의 연결 기능 제공
   - 데이터가 전송되는 최종적인 경로상의 양 끝단 사이의 연결이 완성되는 곳
5. Session Layer
   - 전송 계층과 유사한 매커니즘을 갖고있지만 조금 더 논리의 영역에 가까움
   - 사용자 간의 대화 개념의 연결로 사용
6. Presentation Layer
   - 전송되는 데이터의 의미가 소실되지 않도록 함
   - 압축 및 암호화의 기능도 다룸
7. Application Layer
   - 네트워크 응용 환경을 지원

## Expression of Network Address

식별자(Identifier)의 4가지 기능

- 유일성
- 확장성
- 편리성
- 정보의 함축

IP Address

- IP 프로토콜이 호스트를 구분하기 위하여 사용하는 주소 체계
- 호스트를 인터넷에 연결하려면 반드시 IP주소를 할당 받아야 함
- 8비트씩 네 부분으로 나누어 십진수로 표현

DNS

- 주소와 이름 정보를 자동으로 유지하고 관리하는 분산 데이터베이스 시스템
- 호스트 주소와 이름 정보를 '네임 서버'가 관리
- 주소 변환이 필요한 클라이언트는 네임 서버에 요청해서 IP주소를 얻음

Other Addresses

- MAC 주소
- 포트 주소
- 메일 주소

# Ch 2. Network Basics (2) : Network Models, Network Technology

## Network Models

프로토콜은 모듈화라는 설계과정을 통해 이루어짐

프로토콜에서 중요한 점

- 주소 표현
- 흐름 제어
- 오류 제어
- 전송 방식

### OSI 7 계층

Header Information

- 각 계층에서 올바르게 기능을 수행하기 위해 데이터를 하위 계층으로 이해할 수 있도록 태그를 추가

Intermediary Node

- 데이터를 전송할 때 올바른 경로로 전송하기 위해 존재

