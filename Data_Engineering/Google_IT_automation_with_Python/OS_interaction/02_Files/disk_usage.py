# %%
import shutil

du = shutil.disk_usage('/')
print(du)
# %%
print(du[0])
# %%
print(round(du[2]/du[0]*100,2))
# %%
