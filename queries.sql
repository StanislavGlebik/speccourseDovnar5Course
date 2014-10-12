select dates.date, customers.name, sum(applesAmount) from main
         join shops on shop_id=shops.id
         join dates on date_id=dates.id
         join kinds on kind_id=kinds.id
         join customers on customer_id=customers.id
                  where shops.name = "stash_shop"
                  and kinds.kind = "ranetki"
         group by dates.date, customers.name;


