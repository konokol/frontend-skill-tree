const initialize = window.mermaid.initialize.bind(window.mermaid);
  window.mermaid.initialize = (config = {}) => initialize({
    ...config,
    flowchart: {
      ...config.flowchart,
      curve: "step"
    }
  });