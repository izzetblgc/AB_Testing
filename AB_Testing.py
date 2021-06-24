import itertools
import numpy as np
import pandas as pd
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Control Group")
df_test = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Test Group")

### Satın Alımları AB testine tabi tutacağız. Ortalamalarına bakalım.

df_control["Purchase"].mean() #550.8940587702316
df_test["Purchase"].mean()  # 582.1060966484675

#Hipotez

# H0: Kontrol ve Test gruplarının satın alımı arasında istatiksel olarak anlamlı bir fark yoktur
# H1: Kontrol ve Test gruplarının satın alımı arasında istatiksel olarak anlamlı bir fark vardır

## Varsayım kontrolü ##

#Normallik Varsayımı

# H0: Normallik dağılımı sağlanmaktadır
# H1: Normallik dağılımı sağlanmamaktadır

test_stat, pvalue = shapiro(df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.5891  HO hipotezi reddedilemez.

test_stat, pvalue = shapiro(df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.1541 HO hipotezi reddedilemez.

#Varyans Homojenliği

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df_control["Purchase"],
                           df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p - value = 0.1083  HO hipotezi reddedilemez

# Varsayımlar sağlandığı için paramatrik testi kullanacağız

# H0: Kontrol ve Test gruplarının satın alımı arasında istatiksel olarak anlamlı bir fark yoktur
# H1: Kontrol ve Test gruplarının satın alımı arasında istatiksel olarak anlamlı bir fark vardır

test_stat, pvalue = ttest_ind(df_control["Purchase"],
                              df_test["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value = 0.3493 hipotez reddedilemez. Yani istatiksel olarak
# Kontrol ve Test gruplarının satın alımları arasında istatiksel olarak anlamlı bir fark yoktur


# Karşılaştırdığımız grupların önce normallik varsayımlarını kontrol ettik. Normallik varsayımları
# sağlandı. Varyans homojenliğini de sağlandığı için parametrik testi kullandık. Varyans homojenliği sağlanmasaydı da
# parametrik testi kullanacaktık ama fonksiyonda equal_var argümanını False yapmamız gerekecekti.


# Elimizdeki verilerle önceki özelliğimiz maximum bidding ile yeni özelliğimiz average
# bidding arasında satın alımlar arasında istatiksel olarak anlamlı bir farkın olmadığı görülmüştür.
# Yeni özellikte ortalama olarak 30 birim fazla bir satın alımımız olsa da test sonucunda
# görüyoruz ki bu aksiyon almak için yeterli değildir ve bu fark şans eseri oluşmuş olabilir
# Bir süre sonra eldeki verilerin artmasıyla bu test tekrarlanabilir
# ancak şu aşamada yeni özelliğin satın alım sayısı kırılımında test aşamasında kalması daha iyi olacaktır


#Kontrol ve Test Gruplarının Reklam görüntülenme sayısı kırılımında AB testi

df_control["Impression"].mean() #101711.44906769728
df_test["Impression"].mean() #120512.41175753452

#Ortalamalar arasında çok büyük bir fark yok. Bunu Test Edelim

#Hipotez

# H0: Kontrol ve Test gruplarının reklam görüntüleme sayıları arasında istatiksel olarak anlamlı bir fark yoktur
# H1: Kontrol ve Test gruplarının reklam görüntüleme sayıları arasında istatiksel olarak anlamlı bir fark vardır


#Normallik Varsayımı

# H0: Normallik dağılımı sağlanmaktadır
# H1: Normallik dağılımı sağlanmamaktadır

test_stat, pvalue = shapiro(df_control["Impression"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.3514  HO hipotezi reddedilemez.

test_stat, pvalue = shapiro(df_test["Impression"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.4148  HO hipotezi reddedilemez.

#Varyans Homojenliği

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df_control["Impression"],
                           df_test["Impression"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p - value = 0.4461 HO hipotezi reddedilemez

# Varsayımlar sağlandığı için paramatrik testi kullanacağız

test_stat, pvalue = ttest_ind(df_control["Impression"],
                              df_test["Impression"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.5f' % (test_stat, pvalue))

# p-value = 0.00005 HO hipotezi reddedilir.
# Yani kontrol ve Test gruplarının reklam görüntüleme sayıları arasında istatiksel olarak
# anlamlı bir fark vardır.






