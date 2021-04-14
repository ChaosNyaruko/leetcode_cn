type Trie struct {
	children []*Trie
	isword   bool
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{
		children: make([]*Trie, 26),
		isword:   false,
	}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	p := this
	for _, c := range word {
		if p.children[c-'a'] == nil {
			c_ := Constructor()
			p.children[c-'a'] = &c_
		}
		p = p.children[c-'a']
	}
	p.isword = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	p := this
	for _, c := range word {
		if p.children[c-'a'] == nil {
			return false
		}
		p = p.children[c-'a']
	}
	return p.isword
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	p := this
	for _, c := range prefix {
		if p.children[c-'a'] == nil {
			return false
		}
		p = p.children[c-'a']
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
