#!/usr/bin/env python3
"""Deus VectorMesh — 30-Second Standalone Quickstart
Runs in pure Python 3 standard library with zero external dependencies.
"""

from module import DeusVectorMesh

def main():
    print("=" * 60)
    print("⚡ Deus VectorMesh — Pure Python In-Memory Vector Database")
    print("=" * 60)

    # 1. Initialize the vector mesh (dimension=3 for demonstration)
    mesh = DeusVectorMesh(dim=3)
    print("✓ Initialized DeusVectorMesh (dim=3, zero dependencies)")

    # 2. Insert sample document vectors
    documents = [
        ("doc_1", [0.95, 0.05, 0.02], {"title": "Quantum Physics Overview", "category": "science"}),
        ("doc_2", [0.91, 0.08, 0.03], {"title": "Particle Mechanics Guide", "category": "science"}),
        ("doc_3", [0.02, 0.94, 0.05], {"title": "Global Macro Economics", "category": "finance"}),
        ("doc_4", [0.04, 0.89, 0.08], {"title": "Bond Yield Curve Analysis", "category": "finance"}),
    ]

    for doc_id, vec, meta in documents:
        mesh.insert(doc_id, vec, meta)
        print(f"  + Indexed: {doc_id} -> '{meta['title']}'")

    print(f"\n✓ Total vectors indexed: {mesh.count()}")

    # 3. Perform a semantic nearest-neighbor query
    query_vector = [0.92, 0.06, 0.04]  # Close to science docs
    print(f"\n🔍 Querying with vector: {query_vector}")
    results = mesh.query(query_vector, top_k=2)

    print("\nTop Matches:")
    for rank, match in enumerate(results, 1):
        print(f"  {rank}. [{match['score']:.4f}] {match['id']} — {match['metadata']['title']} ({match['metadata']['category']})")

    print("\n✓ Execution completed successfully in pure Python standard library.")

if __name__ == "__main__":
    main()
