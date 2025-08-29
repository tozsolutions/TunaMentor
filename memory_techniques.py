import json
import random
from typing import Dict, List, Any
from datetime import datetime, timedelta

class MemoryTechniques:
    def __init__(self):
        self.mind_maps = {}
        self.memory_palaces = {}
        self.visual_associations = {}
        self.color_codes = {
            "important": "#FF6B6B",      # Kırmızı - Önemli
            "formula": "#4ECDC4",        # Turkuaz - Formül
            "example": "#45B7D1",        # Mavi - Örnek
            "definition": "#96CEB4",     # Yeşil - Tanım
            "warning": "#FFEAA7",        # Sarı - Uyarı
            "connection": "#DDA0DD"      # Mor - Bağlantı
        }

    def create_color_coded_mind_map(self, central_topic: str, subtopics: list, connections: dict = None, colors: dict = None) -> dict:
        """
        # Gelişmiş renk kodlama sistemi
        default_colors = {
            "ana_konu": "#FFDC00",  # Fenerbahçe sarısı
            "onemli": "#FF0000",    # Kırmızı - çok önemli
            "orta": "#FFA500",      # Turuncu - orta önem
            "detay": "#1F2A44",     # Fenerbahçe lacivert
            "ornekler": "#00FF00",  # Yeşil - örnekler
            "formul": "#FF00FF",    # Mor - formüller
            "tanim": "#00FFFF"      # Cyan - tanımlar
        }

        color_scheme = colors or default_colors

        mind_map = {
            "central_topic": central_topic,
            "subtopics": [],
            "visual_elements": [],
            "connections": connections or {},
            "color_scheme": color_scheme,
            "creation_time": datetime.now().isoformat(),
            "study_effectiveness": "Yüksek"
        }
        """
        # The following code is a placeholder as the previous code block was just a docstring.
        # The actual implementation of create_color_coded_mind_map would go here,
        # but it was not provided in the changes.
        # Based on the original create_mind_map, we can infer a structure.
        
        default_colors = {
            "ana_konu": "#FFDC00",  # Fenerbahçe sarısı
            "onemli": "#FF0000",    # Kırmızı - çok önemli
            "orta": "#FFA500",      # Turuncu - orta önem
            "detay": "#1F2A44",     # Fenerbahçe lacivert
            "ornekler": "#00FF00",  # Yeşil - örnekler
            "formul": "#FF00FF",    # Mor - formüller
            "tanim": "#00FFFF"      # Cyan - tanımlar
        }

        color_scheme = colors or default_colors

        mind_map = {
            "central_topic": central_topic,
            "subtopics": [],
            "visual_elements": [],
            "connections": connections or {},
            "color_scheme": color_scheme,
            "creation_time": datetime.now().isoformat(),
            "study_effectiveness": "Yüksek"
        }

        # Ana dalları oluştur (orijinal fonksiyondaki mantığı kullanarak)
        if subtopics:
            for i, subtopic in enumerate(subtopics):
                branch = {
                    "id": f"branch_{len(mind_map['subtopics'])}",
                    "title": subtopic.get("name", f"Alt Konu {i+1}"),
                    "color": color_scheme.get(subtopic.get("type", "detay")), # Varsayılan olarak detay rengini kullan
                    "sub_branches": subtopic.get("details", []),
                    "keywords": subtopic.get("keywords", []),
                    "visual_elements": subtopic.get("visuals", [])
                }
                mind_map["subtopics"].append(branch)

        # Bağlantıları oluştur (orijinal fonksiyondaki mantığı kullanarak)
        mind_map["connections"] = self._create_connections(mind_map["subtopics"])

        # Hafızaya kaydet
        map_id = f"{central_topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.mind_maps[map_id] = mind_map

        return {"map_id": map_id, "mind_map": mind_map}


    def _create_connections(self, branches: List[Dict]) -> List[Dict]:
        """Dallar arası bağlantı oluştur"""
        connections = []

        for i, branch1 in enumerate(branches):
            for j, branch2 in enumerate(branches[i+1:], i+1):
                # Ortak kelimeler varsa bağlantı kur
                common_keywords = set(branch1.get("keywords", [])) & set(branch2.get("keywords", []))
                if common_keywords:
                    connections.append({
                        "from_branch": branch1["id"],
                        "to_branch": branch2["id"],
                        "connection_type": "keyword_similarity",
                        "common_elements": list(common_keywords),
                        "strength": len(common_keywords)
                    })

        return connections

    def create_memory_palace(self, username: str, subject: str, location_type: str = "home") -> Dict:
        """Zihin sarayı oluştur"""
        palace_templates = {
            "home": {
                "name": "Ev Zihin Sarayı",
                "rooms": [
                    {"name": "Giriş Kapısı", "capacity": 2, "type": "introduction"},
                    {"name": "Salon", "capacity": 5, "type": "main_concepts"},
                    {"name": "Mutfak", "capacity": 4, "type": "examples"},
                    {"name": "Yatak Odası", "capacity": 3, "type": "formulas"},
                    {"name": "Banyo", "capacity": 2, "type": "exceptions"},
                    {"name": "Balkon", "capacity": 3, "type": "connections"}
                ],
                "route": ["Giriş Kapısı", "Salon", "Mutfak", "Yatak Odası", "Banyo", "Balkon"]
            },
            "school": {
                "name": "Okul Zihin Sarayı", 
                "rooms": [
                    {"name": "Okul Bahçesi", "capacity": 3, "type": "introduction"},
                    {"name": "Sınıf", "capacity": 6, "type": "main_concepts"},
                    {"name": "Koridor", "capacity": 4, "type": "examples"},
                    {"name": "Kütüphane", "capacity": 5, "type": "formulas"},
                    {"name": "Laboratuvar", "capacity": 3, "type": "experiments"},
                    {"name": "Kantin", "capacity": 2, "type": "summary"}
                ],
                "route": ["Okul Bahçesi", "Sınıf", "Koridor", "Kütüphane", "Laboratuvar", "Kantin"]
            }
        }

        template = palace_templates.get(location_type, palace_templates["home"])

        palace = {
            "palace_id": f"{username}_{subject}_{location_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "username": username,
            "subject": subject,
            "template": template,
            "stored_information": {},
            "created_date": datetime.now().isoformat(),
            "last_accessed": datetime.now().isoformat(),
            "access_count": 0
        }

        self.memory_palaces[palace["palace_id"]] = palace
        return palace

    def store_information_in_palace(self, palace_id: str, information: Dict) -> bool:
        """Bilgiyi zihin sarayına yerleştir"""
        if palace_id not in self.memory_palaces:
            return False

        palace = self.memory_palaces[palace_id]
        rooms = palace["template"]["rooms"]

        for info_item in information.get("items", []):
            # En uygun odayı bul
            best_room = self._find_best_room(rooms, info_item)

            if best_room:
                room_name = best_room["name"]
                if room_name not in palace["stored_information"]:
                    palace["stored_information"][room_name] = []

                # Bilgiyi görsel öğelerle zenginleştir
                enhanced_info = {
                    "content": info_item["content"],
                    "visual_cue": self._create_visual_cue(info_item["content"]),
                    "emotional_tag": self._create_emotional_tag(info_item["content"]),
                    "position": len(palace["stored_information"][room_name]) + 1,
                    "stored_date": datetime.now().isoformat()
                }

                palace["stored_information"][room_name].append(enhanced_info)

        palace["last_accessed"] = datetime.now().isoformat()
        return True

    def _find_best_room(self, rooms: List[Dict], info_item: Dict) -> Dict:
        """Bilgi için en uygun odayı bul"""
        content_type = info_item.get("type", "general")

        type_mapping = {
            "definition": "main_concepts",
            "formula": "formulas", 
            "example": "examples",
            "exception": "exceptions",
            "introduction": "introduction",
            "connection": "connections"
        }

        target_room_type = type_mapping.get(content_type, "main_concepts")

        # Hedef oda tipini bul
        for room in rooms:
            if room["type"] == target_room_type:
                return room

        # Bulunamazsa ilk odayı döndür
        return rooms[0] if rooms else None

    def _create_visual_cue(self, content: str) -> str:
        """İçerik için görsel ipucu oluştur"""
        visual_cues = [
            "🔥 Yanıyor", "⚡ Işıldıyor", "🌈 Renkli", "💎 Parlıyor",
            "🎭 Dans ediyor", "🚀 Uçuyor", "🌊 Dalgalanıyor", "⭐ Pırıldıyor"
        ]

        return random.choice(visual_cues)

    def _create_emotional_tag(self, content: str) -> str:
        """İçerik için duygusal etiket oluştur"""
        emotions = [
            "🎉 Heyecanlı", "😌 Rahatlatıcı", "🤔 Merak uyandıran", 
            "💪 Güç veren", "🎯 Odaklanmış", "✨ İlham verici"
        ]

        return random.choice(emotions)

    def take_mental_walk(self, palace_id: str) -> Dict:
        """Zihinsel yürüyüş yap"""
        if palace_id not in self.memory_palaces:
            return {"error": "Palace not found"}

        palace = self.memory_palaces[palace_id]
        route = palace["template"]["route"]
        stored_info = palace["stored_information"]

        mental_walk = {
            "palace_name": palace["template"]["name"],
            "total_rooms": len(route),
            "route_map": [],
            "total_information": 0
        }

        for room_name in route:
            room_data = {
                "room_name": room_name,
                "information_count": len(stored_info.get(room_name, [])),
                "information_items": stored_info.get(room_name, [])
            }

            mental_walk["route_map"].append(room_data)
            mental_walk["total_information"] += room_data["information_count"]

        # Erişim sayacını artır
        palace["access_count"] += 1
        palace["last_accessed"] = datetime.now().isoformat()

        return mental_walk

    def create_flash_cards(self, subject: str, topic: str, content: List[Dict]) -> List[Dict]:
        """Görsel flash kartlar oluştur"""
        flash_cards = []

        for item in content:
            card = {
                "card_id": f"card_{len(flash_cards)+1}_{datetime.now().strftime('%H%M%S')}",
                "subject": subject,
                "topic": topic,
                "front": {
                    "text": item.get("question", ""),
                    "visual_hint": self._create_visual_hint(item.get("question", "")),
                    "color": self._assign_card_color(subject)
                },
                "back": {
                    "text": item.get("answer", ""),
                    "explanation": item.get("explanation", ""),
                    "memory_aid": self._create_memory_aid(item.get("answer", "")),
                    "related_concepts": item.get("related", [])
                },
                "difficulty": item.get("difficulty", "medium"),
                "last_reviewed": None,
                "review_count": 0,
                "accuracy_rate": 0
            }

            flash_cards.append(card)

        return flash_cards

    def _create_visual_hint(self, text: str) -> str:
        """Metin için görsel ipucu oluştur"""
        if "matematik" in text.lower() or "sayı" in text.lower():
            return "🔢"
        elif "türkçe" in text.lower() or "kelime" in text.lower():
            return "📝"
        elif "fen" in text.lower() or "bilim" in text.lower():
            return "🔬"
        else:
            return "💡"

    def _assign_card_color(self, subject: str) -> str:
        """Derse göre kart rengi ata"""
        subject_colors = {
            "Matematik": "#FF6B6B",
            "Türkçe": "#4ECDC4", 
            "Fen Bilimleri": "#45B7D1",
            "T.C. İnkılap Tarihi": "#96CEB4",
            "Din Kültürü": "#FFEAA7",
            "İngilizce": "#DDA0DD"
        }

        return subject_colors.get(subject, "#95A5A6")

    def _create_memory_aid(self, answer: str) -> str:
        """Cevap için hafıza yardımcısı oluştur"""
        aids = [
            f"🎵 '{answer}' kelimesini şarkı yap!",
            f"🎭 '{answer}' ile hikaye kur!",
            f"🎨 '{answer}' resmini çiz!",
            f"🤝 '{answer}' ile hareket yap!",
            f"🏠 '{answer}' evinde nerede olurdu?"
        ]

        return random.choice(aids)