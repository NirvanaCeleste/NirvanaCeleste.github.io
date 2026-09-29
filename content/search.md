---
title: "搜索"
date: 2026-09-29
description: "站内全文搜索(支持中文)"
sitemap: true
---
<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<div id="pagefind-search"></div>
<script src="/pagefind/pagefind-ui.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", function() {
    new PagefindUI({
      element: "#pagefind-search",
      showImages: false,
      showSubResults: true,
      translations: {
        placeholder: "搜索文章、教程、题解…",
        clear_search: "清除",
        load_more: "加载更多结果",
        search_label: "站内搜索",
        zero_results: '没有找到"[SEARCH_TERM]"的相关内容',
        many_results: '找到 [COUNT] 条"[SEARCH_TERM]"的结果',
        one_result: '找到 [COUNT] 条"[SEARCH_TERM]"的结果',
        searching: '正在搜索"[SEARCH_TERM]"…'
      }
    });
  });
</script>
