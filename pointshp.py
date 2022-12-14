import geopandas as gpd 
fp = "./Point_4888_UID_2/point_4888_UID_2.shp"
data = gpd.read_file(fp)

df1 = data[['UniqueID','FeatureNam','FeatureSta']]
df1 = df1.groupby(['UniqueID','FeatureNam','FeatureSta']).size().reset_index(name="Count")
df1.to_excel("point.xlsx")
print(df1)
