def profit_analyzer(
    china_price:float,
    china_shipping:float,
    weight:float,
    exchange_rate:float=4.5,
    platform_fee:float=0.2,
    business_taxrate:float=0.1,
    target_margin:float=0.3
) -> dict:

    """
    china_price從中國進貨價
    china_shipping中國海快價格
    weight商品重量(KG)
    exchange_rate中國換台幣匯率4.5
    platform_fee 蝦皮平台抽成２０％
    營所稅+營業稅=10%
    target_margin目標毛利30% 
    """
    intl_shipping_rmb = weight*china_shipping

    total_rmb=china_price+intl_shipping_rmb

    total_cost_twd=total_rmb*exchange_rate 

    divisor=1-platform_fee-target_margin-business_taxrate
    suggested_price=total_cost_twd/divisor

    profit=suggested_price*target_margin

    return {
        "總成本":round(total_cost_twd,2),
        "建議售價":round(suggested_price,2),
        "應繳稅收":round(suggested_price*business_taxrate,2),
    
        "實拿純利":round(profit,2),
    }