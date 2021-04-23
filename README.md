Usage:
```
!pip install -e git+https://github.com/sre-fuse/fuse-datasets#egg=fuse-datasets
```

To locate the installed package, we import site 
```
import site
site.main()
```

Import Data Loader
```
from fuse_datasets import data_loader
```

For "Apple-Banana" dataset
```
data, label, _ = data_loader.load_apple_banana()
```

For "Fuse-Face-Dataset"
```
train_data,test_data,train_target,test_target = data_loader.load_face_data()
``` 
