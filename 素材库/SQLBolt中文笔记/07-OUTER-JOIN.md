# SQLBolt 第 7 课：OUTER JOIN 中文学习笔记

来源：[SQLBolt Lesson 7: OUTER JOINs](https://sqlbolt.com/lesson/select_queries_with_outer_joins)

## 一、为什么需要 OUTER JOIN

上一课的 `INNER JOIN` 只保留两张表都能匹配上的行。

如果两张表的数据不对称，例如一张表有新数据、另一张表还没有对应记录，`INNER JOIN` 会把没有匹配的行排除掉，导致结果缺失。

这种情况下，需要使用：

- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL JOIN`

把需要保留的数据完整保留下来。

## 二、语法模板

```sql
SELECT column, another_column, ...
FROM mytable
LEFT JOIN another_table
  ON mytable.id = another_table.matching_id
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

`RIGHT JOIN` 和 `FULL JOIN` 的写法同理。

## 三、三种 JOIN 的语义

### LEFT JOIN

保留左表的全部行。

- 如果右表存在匹配行，就组合右表数据。
- 如果右表没有匹配行，右表字段显示为 `NULL`。

### RIGHT JOIN

保留右表的全部行。

- 如果左表存在匹配行，就组合左表数据。
- 如果左表没有匹配行，左表字段显示为 `NULL`。

### FULL JOIN

保留左右两张表的全部行。

- 只要其中一张表有记录，就会保留。
- 另一边没有匹配时，对应字段为 `NULL`。

## 四、OUTER 关键字的含义

下面两组写法等价：

- `LEFT OUTER JOIN` = `LEFT JOIN`
- `RIGHT OUTER JOIN` = `RIGHT JOIN`
- `FULL OUTER JOIN` = `FULL JOIN`

`OUTER` 主要是为了兼容 SQL-92 语法，不是另一种新连接。

## 五、NULL 警告

使用 OUTER JOIN 后，结果中很可能出现 `NULL`。

后续还需要额外逻辑处理这些 `NULL`，例如：

- 判断是否匹配成功。
- 用 `COALESCE` 或 `IFNULL` 替换空值。
- 在 `WHERE` 中判断字段是否为 `NULL`。

下一课会专门讲 `NULL`。

## 六、第 7 课练习翻译

SQLBolt 练习使用两张表：

- `buildings`
- `employees`

部分建筑是新建筑，还没有员工，但仍然需要在结果中保留。

练习任务：

1. 找出所有有员工的建筑。
2. 列出所有建筑及其容量。
3. 列出所有建筑，以及每栋建筑中不同的员工角色，包括没有员工的建筑。

注意：SQLBolt 的浏览器练习环境只支持 `LEFT JOIN`。

## 七、做题前先判断

1. 哪张表是左表，哪张表是右表？
2. 你要完整保留哪张表的数据？
3. 两张表的匹配键是什么？
4. 没有匹配时，哪些字段会变成 `NULL`？
5. 这题应该用 `INNER JOIN` 还是 `LEFT JOIN`？

## 八、核心结论

- `INNER JOIN`：只保留双方都匹配的数据。
- `LEFT JOIN`：以左表为主，右表没有匹配也保留左表。
- `RIGHT JOIN`：以右表为主。
- `FULL JOIN`：左右两边都保留。
- OUTER JOIN 很容易产生 `NULL`，要单独处理。
