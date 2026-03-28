
## Day 24 — NumPy, Random Data and Basic Statistics  

> Today’s focus: practice creating and manipulating NumPy arrays, generate random data, and apply basic statistical and linear algebra operations with simple visualizations.  
> Author: Luka Marinkovic  

### Working with NumPy arrays  

I created one‑dimensional and two‑dimensional NumPy arrays from Python lists and tuples, and compared them to plain lists. I checked their `dtype`, `shape`, and `size` to understand how NumPy represents data internally. I also converted arrays back to Python lists using `.tolist()` to see how easy it is to move between native types and NumPy structures. This helped me see NumPy arrays as a more powerful, vectorized replacement for lists when doing numerical work.  

### Basic operations, slicing and reshaping  

On the arrays, I tried element‑wise arithmetic like addition, subtraction, multiplication, division, modulo, integer division, and exponentiation. I practised indexing rows and columns in 2D arrays and used slicing to grab sub‑matrices or reverse arrays. I used functions like `reshape`, `flatten`, `hstack`, and `vstack` to change shapes and concatenate arrays. These exercises showed how NumPy can transform and combine data without writing explicit loops.  

### Generating random data and visualizing distributions  

I used NumPy’s random utilities to generate uniform random numbers, random integers in a range, and samples from a normal distribution. With `matplotlib` and `seaborn`, I plotted histograms of normally distributed data to see how the parameters (mean and standard deviation) affect the shape. I also created a simple line plot showing a linear relationship between temperature and pressure. This gave me a first taste of how to simulate data and quickly visualize it for exploration.  

### Statistical functions and linear algebra basics  

On the generated arrays, I applied statistical functions such as `min`, `max`, `mean`, `median`, and `std` to summarize the data. I also used `scipy.stats.mode` to find the most frequent value in a sample. For linear algebra, I computed dot products with `np.dot`, performed matrix multiplication with `np.matmul`, and calculated determinants with `np.linalg.det`. These operations showed how NumPy supports both basic statistics and core linear algebra in a compact, readable way.  

### Patterns, repetition and small utilities  

I experimented with functions like `np.zeros`, `np.ones`, `np.tile`, and `np.repeat` to build structured or repeating numeric patterns. I used `np.arange`, `np.linspace`, and `np.logspace` to generate sequences with different spacing strategies. I also tested boolean arrays and type checking to see how NumPy handles different numeric and logical types. Altogether, these utilities made it clear how quickly I can generate and structure numerical datasets for later analysis or experimentation.