# chat_app/utils.py
from django.core.cache import cache
from .model_providers.openrouter.query import query_openrouter
from .model_providers.prompt_config import prompt_config

def query_provider(prompt: str, model_type: str, model_id: str, language: str = "en"):
    """Возвращает: (content, tokens_used, real_used_model)"""
    cache_key = f"{model_type}_{model_id}_{language}_{hash(prompt)}"
    if cached := cache.get(cache_key):
        return cached[0], cached[1], cached[2]

    config = prompt_config.get(model_type, prompt_config["text"])
    system_prompt = config["default_systems"].get(language, config["default_systems"]["en"])
    
    content, used_model = query_openrouter(
        prompt=prompt,
        model_id=model_id,
        language=language,
        system_prompt=system_prompt,
        temperature=config["temperature"]
    )
    
    tokens_used = len(content) // 4 if content else 0
    cache.set(cache_key, (content, tokens_used, used_model), timeout=3600)
    return content, tokens_used, used_model
# # ai-chat-django/chat_app/utils.py
# from typing import Tuple
# from django.core.cache import cache
# from .types import ModelType
# from .ai_providers.text_models import query_deepseek, query_mistral, query_deephermes
# from .ai_providers.code_models import (
#     query_qwen3_coder,
#     query_llama3_coder,
#     query_deepseek_prover,
# )


# def query_provider(
#     prompt: str, model_type: ModelType, model_name: str, language: str = "en"
# ) -> Tuple[str, int]:
#     """
#     Основной шлюз для всех AI-запросов:
#     1. Проверка кеша
#     2. Маршрутизация к конкретной модели
#     3. Сохранение результатов
#     """
#     cache_key = f"{model_type}_{model_name}_{language}_{hash(prompt)}"
#     if cached := cache.get(cache_key):
#         return cached  # Возврат кешированного результата

#     # Маппинг моделей на обработчики
#     MODEL_MAPPING = {
#         # Текстовые модели
#         "deepseek_qwen3": query_deepseek,
#         "mistral_devstral": query_mistral,
#         "deephermes": query_deephermes,
#         # Модели генерации кода
#         "llama3_coder": query_llama3_coder,
#         "deepseek_prover": query_deepseek_prover,
#         "qwen3_coder": query_qwen3_coder,
#     }

#     if model_name not in MODEL_MAPPING:
#         return f"[Error] Unknown model: {model_name}", 0

#     result = MODEL_MAPPING[model_name](prompt, language)
#     cache.set(cache_key, result, timeout=3600)
#     return result
