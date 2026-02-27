---
name: ReasoningBank Intelligence
description: Implement adaptive learning with ReasoningBank for pattern recognition, strategy optimization, and continuous improvement. Use when building self-learning agents, optimizing workflows, or implementing meta-cognitive systems.
---

# ReasoningBank Intelligence

## When to Use This Skill

- Building self-learning agents that adapt strategies based on accumulated experience
- Implementing meta-learning to discover cross-task optimization principles
- Comparing and selecting optimal strategies across multiple approaches for a task type
- Transferring learned knowledge from one domain to another (e.g., backend to frontend optimization)
- Setting up continuous auto-learning pipelines with confidence thresholds and update schedules

## Prerequisites

- agentic-flow v1.5.11+
- AgentDB v1.0.4+ (for persistence)
- Node.js 18+

## Quick Start

### CLI: Initialize Intelligence Database

```bash
# Initialize AgentDB for ReasoningBank Intelligence
npx agentdb@latest init ./.agentdb/intelligence.db --dimension 1536
claude-flow memory store --key "agentdb/intelligence/init" --value "$(date +%Y-%m-%d)" --namespace agentdb

# Start MCP server for Claude Code integration
npx agentdb@latest mcp
```

### API: Initialize and Record

```typescript
import { ReasoningBank } from 'agentic-flow/reasoningbank';

// Initialize ReasoningBank
const rb = new ReasoningBank({
  persist: true,
  learningRate: 0.1,
  adapter: 'agentdb' // Use AgentDB for storage
});

// Record task outcome
await rb.recordExperience({
  task: 'code_review',
  approach: 'static_analysis_first',
  outcome: {
    success: true,
    metrics: {
      bugs_found: 5,
      time_taken: 120,
      false_positives: 1
    }
  },
  context: {
    language: 'typescript',
    complexity: 'medium'
  }
});

// Get optimal strategy
const strategy = await rb.recommendStrategy('code_review', {
  language: 'typescript',
  complexity: 'high'
});
```

## Core Features

### 1. Pattern Recognition
```typescript
// Learn patterns from data
await rb.learnPattern({
  pattern: 'api_errors_increase_after_deploy',
  triggers: ['deployment', 'traffic_spike'],
  actions: ['rollback', 'scale_up'],
  confidence: 0.85
});

// Match patterns
const matches = await rb.matchPatterns(currentSituation);
```

### 2. Strategy Optimization
```typescript
// Compare strategies
const comparison = await rb.compareStrategies('bug_fixing', [
  'tdd_approach',
  'debug_first',
  'reproduce_then_fix'
]);

// Get best strategy
const best = comparison.strategies[0];
console.log(`Best: ${best.name} (score: ${best.score})`);
```

### 3. Continuous Learning
```typescript
// Enable auto-learning from all tasks
await rb.enableAutoLearning({
  threshold: 0.7,        // Only learn from high-confidence outcomes
  updateFrequency: 100   // Update models every 100 experiences
});
```

## Advanced Usage

### Meta-Learning
```typescript
// Learn about learning
await rb.metaLearn({
  observation: 'parallel_execution_faster_for_independent_tasks',
  confidence: 0.95,
  applicability: {
    task_types: ['batch_processing', 'data_transformation'],
    conditions: ['tasks_independent', 'io_bound']
  }
});
```

### Transfer Learning
```typescript
// Apply knowledge from one domain to another
await rb.transferKnowledge({
  from: 'code_review_javascript',
  to: 'code_review_typescript',
  similarity: 0.8
});
```

### Adaptive Agents
```typescript
// Create self-improving agent
class AdaptiveAgent {
  async execute(task: Task) {
    // Get optimal strategy
    const strategy = await rb.recommendStrategy(task.type, task.context);

    // Execute with strategy
    const result = await this.executeWithStrategy(task, strategy);

    // Learn from outcome
    await rb.recordExperience({
      task: task.type,
      approach: strategy.name,
      outcome: result,
      context: task.context
    });

    return result;
  }
}
```

## Integration with AgentDB

```typescript
// Persist ReasoningBank data
await rb.configure({
  storage: {
    type: 'agentdb',
    options: {
      database: './reasoning-bank.db',
      enableVectorSearch: true
    }
  }
});

// Query learned patterns
const patterns = await rb.query({
  category: 'optimization',
  minConfidence: 0.8,
  timeRange: { last: '30d' }
});
```

## Performance Metrics

```typescript
// Track learning effectiveness
const metrics = await rb.getMetrics();
console.log(`
  Total Experiences: ${metrics.totalExperiences}
  Patterns Learned: ${metrics.patternsLearned}
  Strategy Success Rate: ${metrics.strategySuccessRate}
  Improvement Over Time: ${metrics.improvement}
`);
```

## Best Practices

1. **Record consistently**: Log all task outcomes, not just successes
2. **Provide context**: Rich context improves pattern matching
3. **Set thresholds**: Filter low-confidence learnings
4. **Review periodically**: Audit learned patterns for quality
5. **Use vector search**: Enable semantic pattern matching

## Troubleshooting

### Issue: Poor recommendations
**Solution**: Ensure sufficient training data (100+ experiences per task type)

### Issue: Slow pattern matching
**Solution**: Enable vector indexing in AgentDB

### Issue: Memory growing large
**Solution**: Set TTL for old experiences or enable pruning

---

## Integration with Claude Flow

### Spawn Commands

```bash
# Deploy adaptive learning pipeline for a new domain
claude-flow hive-mind spawn "Initialize ReasoningBank Intelligence for [domain]. \
  Configure pattern recognition with confidence threshold 0.8. \
  Enable auto-learning with update frequency 100. \
  Record baseline strategy comparison for [task_type]." \
  --queen research-strategic \
  --workers coder,researcher

# Run meta-learning analysis across accumulated experiences
claude-flow hive-mind spawn "Analyze all recorded experiences across domains. \
  Identify cross-domain meta-learning patterns. \
  Evaluate transfer learning opportunities between similar domains. \
  Report strategy optimization recommendations." \
  --queen research-strategic \
  --workers researcher,performance-engineer
```

### Memory Storage

```bash
# Store intelligence configuration
claude-flow memory store \
  --key "agentdb/intelligence/config" \
  --value '{"learningRate": 0.1, "threshold": 0.7, "updateFrequency": 100}' \
  --namespace agentdb

# Store strategy comparison results
claude-flow memory store \
  --key "agentdb/intelligence/strategy-results" \
  --value '{"task": "code_review", "best": "static_analysis_first", "score": 0.92}' \
  --namespace agentdb
```

### Related Skills

- **agentdb-vector-search** -- semantic vector search, HNSW indexing
- **agentdb-optimization** -- quantization, HNSW tuning, caching, pruning
- **agentdb-memory-patterns** -- persistent memory, session/long-term storage, consolidation
- **agentdb-learning** -- 9 RL algorithms, training plugins
- **agentdb-advanced** -- QUIC sync, hybrid search, sharding, distance metrics
- **reasoningbank-agentdb** -- trajectory tracking, verdict judgment, memory distillation

---

## Output Templates

### Intelligence Assessment Report

```
REASONINGBANK INTELLIGENCE REPORT
Date: [YYYY-MM-DD]
Domain: [domain]

EXPERIENCE SUMMARY
  Total Experiences: [N]
  Patterns Learned: [N]
  Strategy Success Rate: [%]

STRATEGY COMPARISON ([task_type])
  1. [strategy_name] -- score: [score] -- trials: [N]
  2. [strategy_name] -- score: [score] -- trials: [N]
  ...

META-LEARNING INSIGHTS
  - [observation] (confidence: [score], applies to: [task_types])
  - [observation] (confidence: [score], applies to: [task_types])

TRANSFER LEARNING CANDIDATES
  [source_domain] -> [target_domain] (similarity: [score])

RECOMMENDATIONS
  - [actionable recommendation]
  - [actionable recommendation]
```

---

## Learn More

- ReasoningBank Guide: agentic-flow/src/reasoningbank/README.md
- AgentDB Integration: packages/agentdb/docs/reasoningbank.md
- Pattern Learning: docs/reasoning/patterns.md

---

*Role: Infrastructure. Maintained by PostWach (CTO). Dependencies: reasoningbank-agentdb, agentdb-learning, agentdb-memory-patterns.*
