import tensorflow as tf
for a in /sys/bus/pci/devices/*; do echo 0 | sudo tee -a $a/numa_node; done
tf.config.list_physical_devices("GPU")
