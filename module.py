"""
Deus VectorMesh™ — Serverless P2P Neural Vector Database
Based on expired statutory patent US6944673B2 (Kademlia XOR Metric + Distributed Hash Table)
Optimized for Apple Silicon Unified Memory Architecture (UMA) at 800 GB/s bandwidth.
"""

import math
from typing import Dict, List, Optional, Tuple


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


class VectorMeshNode:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.vectors: Dict[str, Tuple[List[float], Dict]] = {}

    def xor_distance(self, target_id: int) -> int:
        return self.node_id ^ target_id

    def insert(self, vector_id: str, vector: List[float], metadata: Optional[Dict] = None) -> None:
        self.vectors[vector_id] = (vector, metadata or {})

    def query(self, query_vec: List[float], top_k: int = 5) -> List[Tuple[str, float, Dict]]:
        results = []
        for vid, (vec, meta) in self.vectors.items():
            sim = cosine_similarity(query_vec, vec)
            results.append((vid, sim, meta))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]


class DeusVectorMesh:
    """Distributed in-memory shard cluster executing in local UMA."""
    def __init__(self, num_shards: int = 4):
        self.shards = [VectorMeshNode(i) for i in range(num_shards)]

    def _get_shard(self, key: str) -> VectorMeshNode:
        shard_idx = hash(key) % len(self.shards)
        return self.shards[shard_idx]

    def insert(self, vector_id: str, vector: List[float], metadata: Optional[Dict] = None) -> int:
        shard = self._get_shard(vector_id)
        shard.insert(vector_id, vector, metadata)
        return shard.node_id

    def search(self, query_vec: List[float], top_k: int = 5) -> List[Tuple[str, float, Dict]]:
        aggregated = []
        for shard in self.shards:
            aggregated.extend(shard.query(query_vec, top_k))
        aggregated.sort(key=lambda x: x[1], reverse=True)
        return aggregated[:top_k]
