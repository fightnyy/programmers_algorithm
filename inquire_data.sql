--mysql은 기본적으로 대소문자를 구분하지 않지만 where 절에 binary를 붙이면 대소문자를 구분한다. 
-- 예시 : mysql> SELECT * FROM ip2nationCountries WHERE BINARY country LIKE '%Uni%';


-- id로 정렬하기
-- 코드를 입력하세요
SELECT *
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID

-- id의 역순으로 정렬하기 
-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- INTAKE_CONDITION이 Sick 인 동물들 SQL에서는 ==가 아니라 =로 표현
-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID

-- 아프지 않은 동물들 찾기
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'AGED'
ORDER BY ANIMAL_ID


-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- NAME이 같으면 DATETIME을 큰 거 먼저 보여줘라 
-- 여기서 NAME에 ASC가 들어가 있어도 되고 없어도 된다.
-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME,DATETIME
FROM ANIMAL_INS
ORDER BY NAME , DATETIME DESC


--mysql은 상위 몇개라고 할 때 
--우선 order by로 정렬하고
--limit 연산자를 통해 추출 한다. 
--또는 all 연산자로도 풀이할 수 있다. 
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME <= all(select DATETIME from ANIMAL_INS)

SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME 
LIMIT 1


-- 최댓값 구하기 The MAX() function returns the maximum value in a set of values.
-- 코드를 입력하세요
SELECT MAX(DATETIME)
FROM ANIMAL_INS


-- 코드를 입력하세요  The MIN() function returns the minimum value in a set of values.
SELECT MIN(DATETIME)
FROM ANIMAL_INS

--숫자 세기
-- 코드를 입력하세요
SELECT count(*)
FROM ANIMAL_INS



-- 코드를 입력하세요
-- distinct 는 중복 제거
SELECT count(distinct NAME)
FROM ANIMAL_INS

-- 코드를 입력하세요
-- ORDER BY는 가장 마지막에 위치하지만 LIMIT보다는 앞에 위치해야함
SELECT ANIMAL_TYPE,count(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- DATETIME TYPE FIELD 에서 데이터를 얻어내는 방법
-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, COUNT(*) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR >= 9 and HOUR < 20
ORDER BY HOUR



-- 코드를 입력하세요
-- 지역변수 set @hour의 존재 앎
set @hour := -1;

select (@hour := @hour+1) as HOUR, 
(select count(*) from ANIMAL_OUTS where HOUR(DATETIME) = @hour) as COUNT
from ANIMAL_OUTS
where @hOUR<23;


-- null 인것 찾는것
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL

-- null이 아닌것 찾는것
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- ifnull statement 
-- 만약 null이 아니면 그냥 이름을 나타내고 null 이면 No name이 나온다.
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IF (NAME IS NULL, "No name", NAME)as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS


/*
테이블을 볼수 있는 명령어 : show tables;
테이블의 이름을 바꿀 수 있는 명령어 : Rename tables old_name to new_name
*/


/*
join 문에 관한 설명
select *
from Table_A, Table_B
이렇게 해서 결과물을 보면 우리가 일반적으로 생각한 join문은 어떤 필드가 같은것끼리 
연관지어서 나오는것을 생각하는데 결과물을 보면 전혀 그렇지 않고 Table_A의 갯수가 5개 Table_B의 갯수가 3개라고 하면
총 15개의 결과 물이 나온다. 
따라서 어떻게 join을 할것인 mysql에게 알려주는 on 을 사용해야한다.
*/

/*
animal_ins와 animal_outs를 합쳐
그런데 기준(ON)은 animal_ins와 animal_outs의 animal_id가 같은것끼리 합치는 거야
*/
select *
from animal_ins
left join animal_outs
on animal_ins.animal_id = animal_outs.animal_id
order by animal_outs.animal_id


/*
ANIMAL_INS 와 ANIMAL_OUTS 에서 ANIMAL_ID가 같은것끼리 우선 묶는데 여기서 
들어온 날짜보다 나간날짜가 더 늦으면(크면) 이상한것이니까 이것을 뽑아라 
근데 들어온 날짜가 빠른 순으로 뽑아라
*/
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME


/*
ANIMAL 중에 아직 까지 입양 가지 못한것 
그중에 가장 오랫동안 못간것 
*/
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON B.ANIMAL_ID = A.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3

/*
LIKE 사용
or
Not Like 사용
*/
SELECT A.ANIMAL_ID , A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE '%Intact%' and (B.SEX_UPON_OUTCOME LIKE '%Neutered%' or B.SEX_UPON_OUTCOME LIKE '%Spayed%')
ORDER BY A.ANIMAL_ID


/*
우유와 요거트
*/
SELECT Distinct A.CART_ID
FROM CART_PRODUCTS A LEFT JOIN CART_PRODUCTS B ON B.CART_ID = A.CART_ID
WHERE A.NAME = 'MILK' AND B.NAME = 'YOGURT'
ORDER BY A.CART_ID