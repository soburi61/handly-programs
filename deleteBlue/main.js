// MutationObserverのコールバック関数
let observer = new MutationObserver(mutations => {
    mutations.forEach(mutation => {
        // 追加されたノードを取得
        let addedNodes = mutation.addedNodes;

        // 追加されたノードに対して処理を行う
        addedNodes.forEach(node => {
            // <svg aria-label="Verified account">を含む要素を取得
            let verifiedElements = node.querySelectorAll('svg[aria-label="Verified account"]');

            // すべての要素に対して処理を行う
            verifiedElements.forEach(element => {
                // 一番近い親の<div data-testid="cellInnerDiv">を取得
                let parentDiv = element.closest('div[data-testid="cellInnerDiv"]');

                // 親の<div data-testid="cellInnerDiv">が存在する場合、その要素を削除
                if (parentDiv) {
                    parentDiv.remove();
                }
            });
        });
    });
});

// MutationObserverの設定
let config = { childList: true, subtree: true };

// MutationObserverを開始
observer.observe(document, config);