Here are simple Python programs using CSV files, Matplotlib graphs, and Seaborn graphs for your practical examination.

We will use one `data.csv` file for all programs.

## 1. Sample data.csv file

Create a file named `data.csv`.

```
Name,Study_Hours,Marks,Age
A,2,40,20
B,4,50,21
C,6,60,22
D,8,70,23
E,10,80,24
```

## 2. Matplotlib graph programs

First install the libraries:

```
pip install pandas matplotlib seaborn
```

### Program 1: Line Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.plot(data["Study_Hours"], data["Marks"], marker="o")plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Line Graph")plt.show()
```

### Program 2: Bar Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.bar(data["Name"], data["Marks"])plt.xlabel("Name")plt.ylabel("Marks")plt.title("Bar Graph")plt.show()
```

### Program 3: Scatter Plot

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.scatter(data["Study_Hours"], data["Marks"])plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Scatter Plot")plt.show()
```

### Program 4: Histogram

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.hist(data["Marks"], bins=5)plt.xlabel("Marks")plt.ylabel("Frequency")plt.title("Histogram")plt.show()
```

### Program 5: Pie Chart

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.pie(data["Marks"], labels=data["Name"], autopct="%1.1f%%")plt.title("Pie Chart")plt.show()
```

### Program 6: Box Plot

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.boxplot(data["Marks"])plt.ylabel("Marks")plt.title("Box Plot")plt.show()
```

### Program 7: Area Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.fill_between(data["Study_Hours"], data["Marks"])plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Area Graph")plt.show()
```

## 3. Seaborn graph programs

First import the libraries:

```
import pandas as pdimport seaborn as snsimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")
```

### Program 1: Line Plot

```
sns.lineplot(data=data, x="Study_Hours", y="Marks", marker="o")plt.title("Line Plot")plt.show()
```

### Program 2: Bar Plot

```
sns.barplot(data=data, x="Name", y="Marks")plt.title("Bar Plot")plt.show()
```

### Program 3: Scatter Plot

```
sns.scatterplot(data=data, x="Study_Hours", y="Marks")plt.title("Scatter Plot")plt.show()
```

### Program 4: Histogram

```
sns.histplot(data=data, x="Marks", bins=5)plt.title("Histogram")plt.show()
```

### Program 5: Box Plot

```
sns.boxplot(data=data, y="Marks")plt.title("Box Plot")plt.show()
```

### Program 6: Violin Plot

```
sns.violinplot(data=data, y="Marks")plt.title("Violin Plot")plt.show()
```

### Program 7: Heatmap (Correlation)

```
sns.heatmap(data.select_dtypes(include="number").corr(),            annot=True, cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

### Program 8: Pair Plot

```
sns.pairplot(data)plt.show()
```

### Program 9: Count Plot

```
sns.countplot(data=data, x="Name")plt.title("Count Plot")plt.show()
```

### Program 10: Regression Plot

```
sns.regplot(data=data, x="Study_Hours", y="Marks")plt.title("Regression Plot")plt.show()
```

## 4. Difference between Matplotlib and Seaborn

| Matplotlib           | Seaborn                        |
| -------------------- | ------------------------------ |
| `plt.plot()`         | `sns.lineplot()`               |
| `plt.bar()`          | `sns.barplot()`                |
| `plt.scatter()`      | `sns.scatterplot()`            |
| `plt.hist()`         | `sns.histplot()`               |
| `plt.boxplot()`      | `sns.boxplot()`                |
| `plt.pie()`          | No direct built-in equivalent  |
| `plt.fill_between()` | `sns` has no direct equivalent |

## 5. Important graphs for practical exams

| Graph           | Purpose                                        |
| --------------- | ---------------------------------------------- |
| Line Graph      | Shows trends                                   |
| Bar Graph       | Compares categories                            |
| Scatter Plot    | Shows relationship between two variables       |
| Histogram       | Shows frequency distribution                   |
| Pie Chart       | Shows percentage                               |
| Box Plot        | Shows distribution and outliers                |
| Area Graph      | Shows changes over time                        |
| Heatmap         | Shows correlation                              |
| Violin Plot     | Shows data distribution                        |
| Pair Plot       | Shows relationships between multiple variables |
| Regression Plot | Shows trend and regression line                |
| Count Plot      | Counts category occurrences                    |

My suggestion: First practise Line, Bar, Scatter, Histogram, Pie, Box, Heatmap and Pair Plot. These are useful graphs to know for your Python data visualization practical.Here are simple Python programs using CSV files, Matplotlib graphs, and Seaborn graphs for your practical examination.

We will use one `data.csv` file for all programs.

## 1. Sample data.csv file

Create a file named `data.csv`.

```
Name,Study_Hours,Marks,Age
A,2,40,20
B,4,50,21
C,6,60,22
D,8,70,23
E,10,80,24
```

## 2. Matplotlib graph programs

First install the libraries:

```
pip install pandas matplotlib seaborn
```

### Program 1: Line Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.plot(data["Study_Hours"], data["Marks"], marker="o")plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Line Graph")plt.show()
```

### Program 2: Bar Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.bar(data["Name"], data["Marks"])plt.xlabel("Name")plt.ylabel("Marks")plt.title("Bar Graph")plt.show()
```

### Program 3: Scatter Plot

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.scatter(data["Study_Hours"], data["Marks"])plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Scatter Plot")plt.show()
```

### Program 4: Histogram

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.hist(data["Marks"], bins=5)plt.xlabel("Marks")plt.ylabel("Frequency")plt.title("Histogram")plt.show()
```

### Program 5: Pie Chart

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.pie(data["Marks"], labels=data["Name"], autopct="%1.1f%%")plt.title("Pie Chart")plt.show()
```

### Program 6: Box Plot

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.boxplot(data["Marks"])plt.ylabel("Marks")plt.title("Box Plot")plt.show()
```

### Program 7: Area Graph

```
import pandas as pdimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")plt.fill_between(data["Study_Hours"], data["Marks"])plt.xlabel("Study Hours")plt.ylabel("Marks")plt.title("Area Graph")plt.show()
```

## 3. Seaborn graph programs

First import the libraries:

```
import pandas as pdimport seaborn as snsimport matplotlib.pyplot as pltdata = pd.read_csv("data.csv")
```

### Program 1: Line Plot

```
sns.lineplot(data=data, x="Study_Hours", y="Marks", marker="o")plt.title("Line Plot")plt.show()
```

### Program 2: Bar Plot

```
sns.barplot(data=data, x="Name", y="Marks")plt.title("Bar Plot")plt.show()
```

### Program 3: Scatter Plot

```
sns.scatterplot(data=data, x="Study_Hours", y="Marks")plt.title("Scatter Plot")plt.show()
```

### Program 4: Histogram

```
sns.histplot(data=data, x="Marks", bins=5)plt.title("Histogram")plt.show()
```

### Program 5: Box Plot

```
sns.boxplot(data=data, y="Marks")plt.title("Box Plot")plt.show()
```

### Program 6: Violin Plot

```
sns.violinplot(data=data, y="Marks")plt.title("Violin Plot")plt.show()
```

### Program 7: Heatmap (Correlation)

```
sns.heatmap(data.select_dtypes(include="number").corr(),            annot=True, cmap="coolwarm")plt.title("Correlation Heatmap")plt.show()
```

### Program 8: Pair Plot

```
sns.pairplot(data)plt.show()
```

### Program 9: Count Plot

```
sns.countplot(data=data, x="Name")plt.title("Count Plot")plt.show()
```

### Program 10: Regression Plot

```
sns.regplot(data=data, x="Study_Hours", y="Marks")plt.title("Regression Plot")plt.show()
```

## 4. Difference between Matplotlib and Seaborn

| Matplotlib           | Seaborn                        |
| -------------------- | ------------------------------ |
| `plt.plot()`         | `sns.lineplot()`               |
| `plt.bar()`          | `sns.barplot()`                |
| `plt.scatter()`      | `sns.scatterplot()`            |
| `plt.hist()`         | `sns.histplot()`               |
| `plt.boxplot()`      | `sns.boxplot()`                |
| `plt.pie()`          | No direct built-in equivalent  |
| `plt.fill_between()` | `sns` has no direct equivalent |

## 5. Important graphs for practical exams

| Graph           | Purpose                                        |
| --------------- | ---------------------------------------------- |
| Line Graph      | Shows trends                                   |
| Bar Graph       | Compares categories                            |
| Scatter Plot    | Shows relationship between two variables       |
| Histogram       | Shows frequency distribution                   |
| Pie Chart       | Shows percentage                               |
| Box Plot        | Shows distribution and outliers                |
| Area Graph      | Shows changes over time                        |
| Heatmap         | Shows correlation                              |
| Violin Plot     | Shows data distribution                        |
| Pair Plot       | Shows relationships between multiple variables |
| Regression Plot | Shows trend and regression line                |
| Count Plot      | Counts category occurrences                    |

My suggestion: First practise Line, Bar, Scatter, Histogram, Pie, Box, Heatmap and Pair Plot. These are useful graphs to know for your Python data visualization practical.
