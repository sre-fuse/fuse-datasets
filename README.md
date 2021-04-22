Usage:
```
!pip install -e git+https://github.com/sre-fuse/fuse-face-detection#egg=fuse-face-detection
```

Load dataset (in google colab):
```
import site
site.main()
from fuse_datasets import data_loader

For "Apple-Banana" dataset
data, label = data_loader.load_apple_banana()

For "Fuse-Face-Dataset"
train_data,test_data,train_target,test_target = data_loader.load_face_data()

``` 