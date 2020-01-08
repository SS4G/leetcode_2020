/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* trimBST(struct TreeNode* root, int L, int R){
    struct TreeNode* trimedLeft = NULL; 
    struct TreeNode* trimedRight = NULL;// = trimBST(root -> right, L, R);
    if (root == NULL) {
        return NULL;
    }

    if (root -> val <= R && root -> val >= L) {
        root -> left = trimBST(root -> left, L, R);
        root -> right = trimBST(root -> right, L, R);
        return root;
    } 
    else if (root -> val > R) {
        return trimBST(root -> left, L, R);
    } 
    else {
        return trimBST(root -> right, L, R);
    }
}