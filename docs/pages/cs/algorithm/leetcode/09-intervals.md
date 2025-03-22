# 区间

## [合并区间](https://leetcode.cn/problems/merge-intervals)

难度：⭐️⭐️⭐️

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

**解法一** 排序

对区间按左值排序，在循环中区间有重叠时合并，右值取最大值，没有重叠时，不合并。

<details>
  <summary>左值排序</summary>
  
  ```java
    public int[][] merge(int[][] intervals) {
        int start = 0;
        int end = 0;
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

