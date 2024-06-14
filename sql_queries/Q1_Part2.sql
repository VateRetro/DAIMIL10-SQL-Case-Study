SELECT
    pc.name AS category_name,
    psc.name AS subcategory_name,
    MIN(pch.standardcost) AS lowest_price,
    MAX(pch.standardcost) AS highest_price,
    MAX(pch.standardcost) - MIN(pch.standardcost) AS price_difference,
    COUNT(p.productid) AS product_count
FROM
    production.productcategory pc
JOIN
    production.productsubcategory psc ON pc.productcategoryid = psc.productcategoryid
JOIN
    production.product p ON p.productsubcategoryid = psc.productsubcategoryid
JOIN
    production.productcosthistory pch ON p.productid = pch.productid
GROUP BY
    pc.name, psc.name
ORDER BY
    pc.name, psc.name;