# ROS Custom Services 101

In this little project(Part of coursework of [The Construct Sim Robot Ignite Academy](http://www.theconstructsim.com/)), I wrote a code to make the **BB8** robot move in a square-like trajectory for a specific number of times.

![BB8 sq_path](https://i.ibb.co/r33B3dT/bb8-excercice.png)

I created a custom service messages of the  **BB8CustomServiceMessage**  type, which is defined here:

```
float64 side         # The distance of each side of the square
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
```
