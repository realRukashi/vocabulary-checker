import streamlit as st

def leven_dist(token1, token2):
    dp = [[0] * (len(token2) + 1) for i in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        dp[i][0] = i
    for i in range(len(token2) + 1):
        dp[0][i] = i
    
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if (token1[i - 1] == token2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[len(token1)][len(token2)]

def loadVocab(file_name): 
    with open(file_name, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = loadVocab('./vocab.txt')   

def main():
    st.title("Vocabulary Corrector")
    word = st.text_input("Vocabulary: ")
    
    if (st.button("Correct")):
        if not word:  
            st.error("⚠️ Idiot alert!!!")  
            return
        
        word = word.lower()
        
        dist = dict()
        for vocab in vocabs:
            dist[vocab] = leven_dist(word, vocab)
        
        sorted_dist = dict(sorted(dist.items(), key = lambda x:x[1])[:20])
        cur = 0
        keys_list = list(sorted_dist.keys())
        
        st.markdown("### **Best fitted:**")
        
        while dist[keys_list[cur]] == dist[keys_list[0]]:
            st.write("-\t", keys_list[cur])
            cur += 1
            
        col1, = st.columns(1)
        
        col1.markdown("### **Distance:**")
        col1.write(sorted_dist)
        
if __name__ == "__main__":
    main()
        
