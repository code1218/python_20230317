/*
	DML
    insert(Create)
    select(Read)
    update(Update)
    delete(Delete)
*/

select * from `order`;

insert into `order`(order_id, product, price, username, email)
values(1, '삼성노트북', 1500000, 'aaa', 'aaa@gmail.com');

insert into `order`
values
	(5, 'LG노트북', 1300000, 'bbb', 'bbb@gmail.com'),
	(6, 'MSI노트북', 1200000, 'bbb', 'bbb@gmail.com'),
	(7, '삼보노트북', 1200000, 'bbb', 'bbb@gmail.com');


