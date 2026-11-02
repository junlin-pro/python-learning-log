total = 0
while True:
    act = float(input("输入酶活性值:"))
    total += act
print(f"总活性：{total}")

act = 35
if act < 20:
    print("低活性")
elif 20 <= act <= 50:
    print("中活性")
else:
    print("高活性")

od_list = [0.52, 0.47, 0.61, 0.38]
od1 = []
for od in od_list:
    od = od + 0.05
    od1.append(od)
print(f"校正后OD值列表:{od1}")

total = 0
while True:
    val = input("输入酶活性值(输入q退出):")
    if val = "q":
        break
      total += float(val)

print(f"总活性值为:{total}")

reagent = {"Tris": 1.0, "EDTA": 0.5, "NaCl": 2.0, "KCl": 1.5}
high_conc = []
for name,conc in reagent.item():
    if conc > 1.0:
        high_conc.append(Conc)
print(high_conc)


第 1 小时 · 先自己写：功能清单——内置 12 个样本（编号+活性），自动分类：≥90 合格 / 80~89 建议复测 / <80 超标
print("=== 样本质量分类统计器 v1.0 ===")
samples = {
    "A01": 85.2, "A02": 92.1, "A03": 78.9, "A04": 88.5,
    "B01": 90.3, "B02": 95.1, "B03": 82.0, "B04": 76.4,
    "C01": 91.7, "C02": 89.9, "C03": 84.3, "C04": 93.0,
}
sample = []
count = 0
for name,a in samples.items()
if a >= 90:
    level = "合格"
    count += 1
    sample.append(name,a)
elif 80 <= a <= 89:
    level = "建议复测"
else 
    level = "超标"
print(f"总计合格样品数为{count}个,样品合格率为{float(count)/len(samples) * 100%,.2f}")

print("=== 样本质量分类统计器 v2.0 ===")

# 需求②：用户自定义合格线阈值
pass_line = float(input("请输入合格线活性值(单位:U/mL):"))

# 三个分类列表 + 总数据列表，全部初始化在循环外
ok = []
retest = []
fail = []
all_act = []

# 需求①：while True 循环手动录入样本
while True:
    sample_id = input("输入样本编号(输入q退出):")
    if sample_id == "q":
        break
    
    act = float(input("输入样本活性值(U/mL):"))
    
    # 按用户设置的合格线进行三级分类
    if act >= pass_line:
        ok.append(sample_id)
    elif act >= 80:
        retest.append(sample_id)
    else:
        fail.append(sample_id)
    
    all_act.append(act)

# 汇总输出 + 空数据防护
if all_act:
    print("\n" + "="*30)
    print(f"合格(≥{pass_line}): {len(ok)} 个 → {ok}")
    print(f"复测(80~{pass_line-0.1:.1f}): {len(retest)} 个 → {retest}")
    print(f"超标(<80): {len(fail)} 个 → {fail}")
    
    avg = sum(all_act) / len(all_act)
    print(f"\n共检测{len(all_act)}个样本")
    print(f"平均活性值: {avg:.1f} U/mL")
    
    pass_rate = len(ok) / len(all_act) * 100
    print(f"样本合格率: {pass_rate:.1f}%")
else:
    print("未录入任何样本数据")

 