# MiniTorch Module 3

<img src="https://minitorch.github.io/_images/match.png" width="100px">

MiniTorch is a teaching library for machine learning engineers who wish to learn about the internal concepts underlying deep learning systems. Specifically, it is a pure Python re-implementation of the Torch API designed to be simple, easy-to-read, tested, and incremental. The final library can run Torch code with minimal changes (at some efficiency cost). The project was developed for the course Machine Learning Engineering at Cornell Tech.

The project is organized into 5 modules. Each module is build upon the precedents.
* [Module-0](https://github.com/Mountagha/Module-0)
* [Module-1](https://github.com/Mountagha/Module-1)
* [Module-2](https://github.com/Mountagha/Module-2)
* [Module-3](https://github.com/Mountagha/Module-3)
* [Module-4](https://github.com/Mountagha/Module-4)

This is [Module-3](https://github.com/Mountagha/Module-3) and it is focus on taking advantage of tensors to write fast code, first on standars CPUs and then GPU.

### Notes

* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module3.html

This module requires `scalar.py`, `tensor_functions.py`, `tensor_data.py`, `tensor_ops.py`, `operators.py`, `module.py`, and `autodiff.py` from Module 2.

You will need to modify `tensor_functions.py` slightly in this assignment.

* Tests:

```
python run_tests.py
```

* Note:

Several of the tests for this assignment will only run if you are on a GPU machine and will not
run on github's test infrastructure. Please follow the instructions to setup up a colab machine
to run these tests.