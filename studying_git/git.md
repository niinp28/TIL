# Git 관련 명령어



- 초기세팅
  - git config --global user.name {유저네임}
  - git config --global user.email {유저이메일}
  - git config --global -l
    - 설정 확인
- git init
  - 깃을 시작한다
- git add {파일}
  - 파일을 staging area에 올려 놓는다.
  - (처음 만든 파일은 깃이 관리를 하기 시작한다)
  - git add .
    - 을 하게되면 해당 폴더의 모든 아이들을 추가한다.
- git status
  - 깃이 관리하고 있는 파일들의 상태를 확인한다.
- git commit -m "메시지"
  - "메시지"라는 변경사항을 담아서 코밋을 남긴다.
- git commit
  - 만 한 경우에는 vim 에디터가 나온다.
  - `i`를 입력하면 insert 모드가 되어 입력이 가능.
  - `esc`를 눌러 insert모드에서 나온다.
  - `:wq`를 입력하여 저장하고 나온다.
  - enter를 누번 눌러 내용을 구체적으로 작성 가능!(additional)
- git log
  - 코밋 상태를 확인한다
  - git log --oneline
    - 코밋 상태를 한줄로 확인한다.
  - git log -{숫자}
    - 숫자개의 코밋만 확인한다.
  - git log --all
    - 다른 branch의 로그까지 전부 보여준다.
  - git log --graph
    - graph 형식으로 log를 관찰할 수 있도록 한다.



### 깃허브와 연결



- git init

- 깃허브 레포지토리 만들기
  - 레포의 주소 복사하기(가운데에 버튼이 있음)

- git remote add origin {url}
  - 깃허브 주소를 'origin'이라는 별명으로 원격 연결하겠다는 의미이다.
- git remote -v
  - 원격으로 어디에 연결되어있는지 확인하는 명령어
- git push origin master
  - origin이란 별명을 가진 깃허브 레포의 master브랜치에 push, 즉 깃허브에 올린다는 의미
- git push -u origin master
  - origin master는 계속 사용하기 위해 설정을 저장한다는 의미.
  - 이후에는 `git push`만 해도 push가 가능



## clone



- git clone {url}

  - 깃이 아닌 상태에서 깃허브의 레포지토리를 복사해 오는 것
  - 최초 1회만 하면 됨.

  1. `git clone {url}` -> 레포 이름으로 폴더를 생성하여서 clone
  2. `git clone {url} .` -> git bash가 실행된 폴더에 clone
  3. `git clone {url} {폴더이름}` -> 폴더이름을 생성하여 clone

  - clone을 했을 때 .git 폴더가 같이 생성되므로 git init은 할 필요 없음.

- git pull

  - 최초의 clone 이후 (또는 이미 깃인 상태에서) 깃허브의 코밋으로 최신화 시킨다.


## branch



- git branch
  - 어떤 브랜치가 존재하는지, *표시가 있는것이 현재 브랜치

- git branch {branch 이름}

  - 브랜치를 만든다.

- git switch {branch 이름}

  - 해당 브랜치로 옮긴다.
  - git switch -c {branch 이름}
    - 브랜치를 **만듦과 동시에** 해당 브랜치로 옮긴다.

- git switch -d {branch 이름}

  - 브랜치를 삭제한다.



- git merge {branch 이름}

  - 현재 브랜치에서 {branch 이름}을 병합시킨다.

  - CONFLICT 상황 발생

    - A'B+AB'=A'B'

    - A'+Ã=CONFLICT 상황

      \- 해결 후 add, commit

      \- vscode에서 어떤 식으로 정렬할지 결정 가능.

      ​	\-\- `code a.txt` 와 같이 명령어를 입력하면 바로 vscode로 연결된다.
  
  - github에서의 CONFLICT 상황
    - a컴퓨터, b컴퓨터, 깃허브가 있음
    - a컴퓨터가 a'으로 수정, 깃허브에 push
    - b컴퓨터가 a~로 수정하고 코밋
    - b컴퓨터가 깃허브를 pull
    - CONFLICT
  
  

## ignore



- `touch .gitignore` 를 생성한다. 확장자는 편하게 txt로 하면 된다.
  - 이 파일 안에 무시하고 싶은 파일을 적어 놓으면 add를 해도
    해당 파일은 무시된다.
- [https://gitignore.io](https://gitignore.io)
  - 이 사이트를 들어가서 유용하게 ignore 관리가 가능하다.
- 위치는 .git 폴더가 보이는 위치에 두면 된다.



## reset

- git reset --hard {돌아가고자 하는 commit의 아이디}
  - 돌아가고자 하는 commit 상태로 돌아간다.




## reflog

- reset한 기록까지 포함하여 모든 commit log를 확인한다.