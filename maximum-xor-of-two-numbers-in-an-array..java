import java.util.*;

class Solution {
    class TrieNode {
        TrieNode[] children;
        public TrieNode() {
            children = new TrieNode[2];
        }
    }

    TrieNode root;

    public Solution() {
        root = new TrieNode();
    }

    public void insert(int num) {
        TrieNode node = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node.children[bit] == null) {
                node.children[bit] = new TrieNode();
            }
            node = node.children[bit];
        }
    }

    public int findMaximumXOR(int[] nums) {
        int max_xor = 0;
        for (int num : nums) {
            insert(num);
            TrieNode node = root;
            int curr_xor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                int toggle_bit = 1 - bit;
                if (node.children[toggle_bit] != null) {
                    curr_xor = (curr_xor << 1) | 1;
                    node = node.children[toggle_bit];
                } else {
                    curr_xor <<= 1;
                    node = node.children[bit];
                }
            max_xor = Math.max(max_xor, curr_xor);
            }
        }
        return max_xor;
    }
}