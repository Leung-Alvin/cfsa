import stylom as st

def main():
    st.delete_train_test_dirs()
    src = "survey"
    dest_1 = "tr"
    dest_2 = "te"
    tr_set,te_set= st.train_test_split(st.get_all_files(src),1)
    st.create_train_test_dirs()
    st.copy_files(src,dest_1,tr_set)
    st.copy_files(src,dest_2,te_set)
    db_name = "not_bad"
    dir_authors = st.get_all_authors(dest_1)
    dir_prints = st.get_prints(dir_authors, dest_1)