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