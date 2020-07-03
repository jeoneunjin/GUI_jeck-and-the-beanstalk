# Final-project_2020810067_전은진
게임 프로그래밍 환경 : Visual Studio Code; Python 3.7(64-bit); Pygame 이용
> 동일한 환경에서 실행해주세요 

게임 실행 준비 : 
--------------
1. 게임 내에 필요한 파일들이 많습니다. 꼭 소스코드 파일과 같은 폴더 안에 다같이 저장되어있는지 확인해주세요
![image](https://user-images.githubusercontent.com/67683170/86439896-6a799480-bd44-11ea-8830-5c35bce29481.png)
> 위 사진에 있는 파일이 모두 있어야 됩니다. 

2. 같은 폴더 안에 저장이 되어 있다면, 이미지와 같은 파일(final project.py)을 열어 게임을 실행하면 됩니다.

<img width = "200" src ="https://user-images.githubusercontent.com/67683170/86303431-bd6d2200-bc46-11ea-9467-46e420c55a82.png">

1.시작 화면 : 
----------------
처음 화면은 사진과 같이 잭과 콩나무 배경과 play 버튼이 나옵니다.
![image](https://user-images.githubusercontent.com/67683170/86304472-e216c900-bc49-11ea-8678-4eff46ee2778.png)
<div>
<img width = "200" src="https://user-images.githubusercontent.com/67683170/86442391-b29ab600-bd48-11ea-82f9-c6bf6b23bbf7.jpg">
<img width = "200" src ="https://user-images.githubusercontent.com/67683170/86442394-b3334c80-bd48-11ea-8fbe-bce9abe9c039.jpg">
</div>
> 마우스가 버튼 위에 위치해 있을 때 버튼의 색이 밝은 초록색으로 변합니다.

> play!가 적혀 있는 초록색 버튼을 누르면 게임 설명 화면으로 넘어갑니다.

2.게임 설명 화면 :
----------
![image](https://user-images.githubusercontent.com/67683170/86440503-86ca0100-bd45-11ea-8342-7736d53f9961.png)
게임 설명은 사진으로 대체했습니다. 위 사진의 모습과 같이 나옵니다.
> 'spacebar'를 누르면 카운트 다운 화면으로 넘어갑니다.

3.카운트 다운과 게임 시작 :
----------
![image](https://user-images.githubusercontent.com/67683170/86446202-98fc6d00-bd4e-11ea-9fe0-1eef8e886f74.png)

> 카운트 다운 중 화면입니다.

![image](https://user-images.githubusercontent.com/67683170/86440685-de686c80-bd45-11ea-9597-eb804ce53d5a.png)

> 위 사진은 카운트 다운 후 화면입니다. 화면에서 보이는 그림과 같이 창 X 버튼을 눌러 해당 창을 꺼야 게임이 시작됩니다. 

4.게임 플레이:
----------
<div>
<img width ="400" src = "https://user-images.githubusercontent.com/67683170/86441021-7ebe9100-bd46-11ea-9a5f-b422035133b6.png">
<img width ="400" src ="https://user-images.githubusercontent.com/67683170/86443513-559fff80-bd4a-11ea-831e-3d7fec742de4.png" > 
</div>

> 플레이 중 사진입니다.

<img src="https://user-images.githubusercontent.com/67683170/86443229-f3df9580-bd49-11ea-9e18-e30a074fba82.png">

+ 제한 시간은 20초로 설정했습니다.

+ 날아오는 장애물은 새와 거인이 던지는 돌입니다. 

+ 화면에서 장애물들이 사라지면 다른 랜덤한 곳에서 재생성됩니다. 

+ 잭은 위, 아래, 오른쪽, 왼쪽으로 이동할 수 있습니다. 

+ 잭이 보이는 화면보다 왼쪽 또는 오른쪽으로 갔을 때, 장애물과 부딪쳤을 때 게임오버 화면으로 넘어갑니다.

4-1 잭의 움직임, 장애물의 움직임, timer:
----------
1. 잭의 움직임 :

![image](https://user-images.githubusercontent.com/67683170/86444320-8af91d00-bd4b-11ea-9ddc-3322c85dc021.png)

> 캐릭터가 실제로 움직여서 이동하는 것처럼 보이도록 구현하기 위해서 연속적인 모션의 그림을 그리고 해당 그림이 순서대로 화면에 출력되도록 코드를 작성했습니다. 

2. 장애물의 움직임 :
![image](https://user-images.githubusercontent.com/67683170/86444868-6487b180-bd4c-11ea-9e59-24d3cbaa66ad.png)

> 새와 돌의 초기 위치입니다.

![image](https://user-images.githubusercontent.com/67683170/86445138-d4963780-bd4c-11ea-8a57-6e1f38360df0.png)

> 새와 돌이 한번 화면에 출력되어 나와서 이동 후 화면 밖으로 나가게 된다면 다음과 같이 랜덤하게 위치를 바꿔줍니다.

+ 새와 돌은 잭의 움직임 또는 게임 사용자와 상관없이 자동으로 일정하게 이동합니다.

> 새와 돌이 각각 x값이 일정하게 감소, y값이 일정하게 증가하도록 게임 루프안에 코드를 작성했습니다.

3. timer :
+ 게임 플레이 중 왼쪽 상단에 남은 시간을 확인할 수 있습니다.

5.게임오버 화면 :
----------
![image](https://user-images.githubusercontent.com/67683170/86446365-d19c4680-bd4e-11ea-92d0-41713a6301c9.png)

> 게임오버 화면입니다.

+ 'R' 키를 누르면 게임이 재시작됩니다.

+ 'Q' 키를 누르면 게임이 종료되어 창이 닫힙니다. 

5.게임성공 화면 :
----------
![image](https://user-images.githubusercontent.com/67683170/86446911-89315880-bd4f-11ea-8333-e6c4069e2877.png)

> 제한시간 내에 게임오버가되지 않았을 때의 화면입니다.

+ 그림과 같이 5초 후 꺼진다는 문구와 성공을 알리는 문구가 출력됩니다.
+ 5초 후 창이 닫힙니다. 

6.기타 :
----------
1. 음악 :

+ 처음 시작할 때 게임 시작화면부터 카운트 다운 후 start 화면까지 backmusic.mp3가 재생됩니다.

> 게임오버 후 재시작하면 규칙화면부터 게임 플레이 화면까지 music.mp3가 재생됩니다.

+ 게임 플레이 화면에서는 music.mp3가 재생됩니다.

+ 게임성공 화면에서는 박수 소리 Applause.wav가 재생됩니다.

2. 배경그림, 캐릭터, 장애물 :

+ 직접 그린 그림들입니다.

+ 장애물과 캐릭터의 배경은 투명하게하여 화면에 자연스럽게 나올 수 있도록 하였습니다. 

**이상으로 기말 프로젝트 : 'jeck and the beanstalk' 게임 설명을 마치겠습니다. 감사합니다 :)**
