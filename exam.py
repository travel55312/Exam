def Cal_Fin_Amnt(Org_Amnt, periods, periods_rt):
    Fin_Amnt = round(Org_Amnt * ((1 + periods_rt) ** periods) ,0)
    Fin_Amnt = "{:,.0f}".format(Fin_Amnt)
    return Fin_Amnt

TestResult = Cal_Fin_Amnt(500000, 24, 0.06)
print(f"期滿後累積的金額為: {TestResult} 元")