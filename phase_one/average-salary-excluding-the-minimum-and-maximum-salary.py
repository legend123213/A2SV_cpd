class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = salary[0]
        max_sal = salary[0]
        s = 0
        for i in salary:
            if i>max_sal:
                max_sal=i
            if i<min_sal:
                min_sal=i
            s+=i
        av = s-max_sal-min_sal
        return round(av/(len(salary)-2),5)