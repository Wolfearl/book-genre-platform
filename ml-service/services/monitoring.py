import logging
from datetime import datetime
from typing import Dict

from django.core.cache import cache

logger = logging.getLogger(__name__)


class PredictionMonitor:
    def __init__(self):
        self.cache_key = "prediction_stats"
        self._init_stats()

    def _init_stats(self):
        """Initializing statistics"""
        default_stats = {
            'total_predictions': 0,
            'successful_predictions': 0,
            'failed_predictions': 0,
            'average_time': 0,
            'last_prediction': None,
            'predictions_today': 0,
            'last_reset': datetime.now().isoformat()
        }
        if not cache.get(self.cache_key):
            cache.set(self.cache_key, default_stats, None)  # Indefinite storage

    def record_prediction(self, success: bool, prediction_time: float):
        """Recording prediction statistics"""
        stats = cache.get(self.cache_key, {})
        stats['total_predictions'] = stats.get('total_predictions', 0) + 1

        if success:
            stats['successful_predictions'] = stats.get('successful_predictions', 0) + 1
        else:
            stats['failed_predictions'] = stats.get('failed_predictions', 0) + 1

        # Updating the average time
        current_avg = stats.get('average_time', 0)
        total_successful = stats.get('successful_predictions', 1)
        if total_successful == 0:
            total_successful = 1
        stats['average_time'] = (current_avg * (total_successful - 1) + prediction_time) / total_successful

        stats['last_prediction'] = datetime.now().isoformat()

        # Reset the counter for the day if necessary
        last_reset = datetime.fromisoformat(stats.get('last_reset', datetime.now().isoformat()))
        if datetime.now().date() > last_reset.date():
            stats['predictions_today'] = 0
            stats['last_reset'] = datetime.now().isoformat()

        if success:
            stats['predictions_today'] = stats.get('predictions_today', 0) + 1

        cache.set(self.cache_key, stats, None)

    def get_stats(self) -> Dict:
        """Getting current statistics"""
        stats = cache.get(self.cache_key, {})
        return stats


# Global Monitor instance
prediction_monitor = PredictionMonitor()