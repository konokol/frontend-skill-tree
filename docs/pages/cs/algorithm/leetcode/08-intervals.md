# 区间

## [56. 合并区间](https://leetcode.cn/problems/merge-intervals)

难度：⭐️⭐️⭐️

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

**解法一** 排序

对区间按左值排序，在循环中区间有重叠时合并，右值取最大值，没有重叠时，不合并。

<details>
  <summary>左值排序</summary>
  
  ```java
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (int[] a, int[] b) -> {
            return a[0] - b[0];
        });
        List<int[]> resultList = new ArrayList<>();
        resultList.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] range = intervals[i];
            int[] merged = resultList.get(resultList.size() - 1);
            if (range[0] > merged[1]) {
                resultList.add(range);
            } else {
                merged[1] = Math.max(range[1], merged[1]);
            }
        }
        return resultList.toArray(new int[resultList.size()][]);
    }
  ```
</details>

## [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/description/)

难度：⭐️⭐️⭐️

给定一个区间的集合 `intervals` ，其中 `intervals[i] = [starti, endi]` 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

**注意** 只在一点上接触的区间是 **不重叠的**。例如 `[1, 2]` 和 `[2, 3]` 是不重叠的。

 

**示例 1:**

**输入:** intervals = [[1,2],[2,3],[3,4],[1,3]]
**输出:** 1
**解释:** 移除 [1,3] 后，剩下的区间没有重叠。

**示例 2:**

**输入:** intervals = [ [1,2], [1,2], [1,2] ]
**输出:** 2
**解释:** 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

**示例 3:**

**输入:** intervals = [ [1,2], [2,3] ]
**输出:** 0
**解释:** 你不需要移除任何区间，因为它们已经是无重叠的了。
 

**提示:**

- `1 <= intervals.length <= 105`
- `intervals[i].length == 2`
- `-5 * 104 <= starti < endi <= 5 * 104`

**解法一** 分组思想

反向思考，题目中说移除最少的区间使得剩余的区间不重叠，可以转换成保留最多的区间并且区间都不重叠。
解题过程
先将这些区间按区间终点排序，按照排序的区间终点划线，则所有的区间可以被分成N组，每组会有 1~若干个区间，由于每一组的区间必定是重叠的（终点相同），要使选中的区间都不重叠，每组至多选一个值，分 2 种情况：
当前分组中，至少存在一个区间，和上一组不重叠，选择任意一个满足条件的区间即可，例如下图中的第二组；
当前分组中，所有区间都和上一组重叠了，则这一组的区间都不选，例如下图中的第三组；

```
    
    第一组：
        ====== ✅
           ===
            == 
      ========
    第二组：
          ========= ❌                  
    =============== ❌
                === ✅
                 ==
    第三组：
                 ====== ❌
            =========== ❌

                ...

    第 N 组：
                          ========= ✅                 
              =====================
                                ===

```

遍历完所有的区间之后，每一组选中的区间记个数，就是可以保留的最大区间数了。

那么，如何定义每一组呢？我们选定排序的区间的右值作为组的分割线，用right来标记当前遍历的组的右边界，初始值就是第一组的区间终点，即 intervals[0][1]。遍历过程中，找到满足条件的区间后，选中它（保留区间数加一），右边界移动到下一组。


<details>
    <summary>分组</summary>

    ```java
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (int[] a, int[] b) -> {
            return a[1] - b[1];
        });
        int right = intervals[0][1];
        int keep = 1;
        for (int[] interval : intervals) {
            if (interval[0] >= right) {
                keep++;
                right = interval[1];
            }
        }
        return intervals.length - keep;
    }
    ```

</details>