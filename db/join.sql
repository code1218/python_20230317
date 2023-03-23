insert into `user` 
values 
	 (1, 'aaa', 'aaa@gmail'),
	 (2, 'bbb', 'bbb@gmail');
     
     
insert into `product`
values
	(0, '삼성노트북', 1500000),
	(0, 'LG노트북', 1400000),
	(0, 'MSI노트북', 1300000),
	(0, '삼보노트북', 1200000);

insert into `order`
values (0, 3, 4);

select * from `order`;

select * from `product`;
     
select * from `user`;

select
	od.order_id,
    od.product_id,
    p.product_id,
    p.product_name,
    p.product_price,
    od.user_id,
    u.user_id,
    u.username,
    u.email
from
	`order` od
    left outer join `product` p on(p.product_id = od.product_id)
    left outer join `user` u on(u.user_id = od.user_id)
where
	od.product_id = 1;
