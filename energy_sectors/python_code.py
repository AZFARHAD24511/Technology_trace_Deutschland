import pandas as pd

# بارگذاری داده‌ها از فایل CSV
df = pd.read_csv('io_tables_de_timeseries_1.csv')

years = [2010, 2015, 2021, 2022]
intensity = {}  # دیکشنری برای ذخیره نسبت‌ها

for year in years:
    # فیلتر ردیف‌های مربوط به برق مصرفی در تولید (مصرف میانی همه‌ی شاخه‌ها)
    elec_consumption = df[
        (df['time'] == year) &
        (df['2_variable_attribute_label'] == 'Input of all homogeneous branches') &
        (df['3_variable_attribute_label'] == 'Electric current,supply of electr.,steam,air cond.')
    ]['value'].sum()
    
    # محاسبه مجموع ارزش تولید (Basic Prices) در آن سال
    production_value = df[
        (df['time'] == year) &
        (df['value_variable_label'] == 'Domestic production (basic prices)')
    ]['value'].sum()
    
    # محاسبه نسبت (بر حسب یک مقدار یورو تولید)
    intensity[year] = elec_consumption / production_value

# نمایش نتایج
for year in years:
    value = intensity[year]
    print(f"{year}: {value:.4f} (≈ {value*100:.2f}%)")

