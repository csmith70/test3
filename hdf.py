import h5py as hdf
filename = 'OMI.he5'
f = hdf.File(filename, mode='r')
dset = f['HDFEOS']
#for name in f:
	#print(name)
#ozone=f['HDFEOS/GRIDS/OMI Column Amount O3/Data Fields/ColumnAmountO3'][0,:,:]
#print(f
for name in dset:
	print(name)
for key in dset.keys():
	print(key)
data = dset['GRIDS']
for new in data.keys():
	print(new)
print(list(data.attrs.keys()))
