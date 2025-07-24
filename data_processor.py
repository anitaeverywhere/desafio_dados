

import collections
import re
from typing import List, Dict, Any, Tuple

def process_data(all_posts: List[Dict[str, Any]], user_id: int) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:

    filtered_posts = [post for post in all_posts if post.get('userId') == user_id]
    total_posts = len(filtered_posts)
    soma_body = sum(len(post.get('body', '')) for post in filtered_posts)
    avg_body_length = soma_body / total_posts if total_posts > 0 else 0
    all_titles = " ".join([post.get('title', '') for post in filtered_posts])
    words = re.findall(r'\b\w{4,}\b', all_titles.lower())
    word_counts = collections.Counter(words).most_common(3)
    statistics = {
        'total_posts': total_posts,
        'avg_body_length': avg_body_length,
        'top_words': word_counts
    }
    return filtered_posts, statistics