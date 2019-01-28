import pandas
li = ['Price or Cost', 'Storage Space', 'Camera', 'Looks']

class PairwiseComparison:
    def __init__(self, li):
        self.df = pandas.DataFrame(1.0, columns=li, index=li)
        
    def pairwise(self):
        ## Pair-wise comparison
        z = len(li)
        col = 0
        row = 0
        while row < z:
            while col < z:    
                if col != row:
                    print('Comparing\n A: {}\nTO\n B: {}'.format(li[row], li[col]))
                    answer = float(input('ENTER: '))
                    self.df[li[col]][li[row]] = answer
                    self.df[li[row]][li[col]] = 1 / answer
                col += 1   
            row += 1
            col = row
            
        # Copy for calculating the criteria weight
        df2 = self.df.copy()
        df2.loc[:, li] = df2.loc[:, li].div(df2.sum(axis=0), axis=1)
        df2['Criteria Weight'] = df2.mean(axis=1)

        # Shrink the df
        df2 = df2['Criteria Weight']

        # Calculate the original df
        self.df = pandas.DataFrame(self.df.values*df2.values, columns=self.df.columns, index=self.df.index)
        self.df['Weighted Sum Value'] = self.df.sum(axis=1)

        # Join
        self.df = self.df.join(df2)
        del df2

    def save(self, dest):
        self.df.to_csv(dest)
        
    def __exit__(self):
        del df

if __name__ == '__main__':
    x = PairwiseComparison(li)
    x.pairwise()
