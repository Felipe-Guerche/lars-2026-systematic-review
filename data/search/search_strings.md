# Search strings

Final search/update date: **3 November 2025**.

## Scopus

### String 1

```text
TITLE-ABS-KEY(("large language model" OR LLM) W/5 robot*) OR TITLE-ABS-KEY(("large language model" OR LLM) W/5 "autonomous agent") AND TITLE-ABS(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic")
```

### String 2

```text
TITLE-ABS((("vision" OR "visual") AND ("language" OR "linguistic")) AND (("Large Language Model" OR "LLM") W/8 ("robot*" OR "action")) AND ("Hallucination" OR "alignment" OR "Grounding"))
```

### String 3

```text
("Mobile Robot" OR "Autonomous Robot") AND ("Hospital Logistics" OR "Healthcare Environment" OR "Critical Domain") AND ("ROS 2" OR Gazebo)
```

## IEEE Xplore

### String 1

```text
((("All Metadata":"large language model" OR "All Metadata":LLM) NEAR/5 "All Metadata":robot*) OR (("All Metadata":"large language model" OR "All Metadata":LLM) NEAR/5 "All Metadata":"autonomous agent")) AND ("Document Title":pddl OR "Document Title":"formal verification" OR "Document Title":grounding OR "Document Title":hallucination OR "Document Title":"neuro-symbolic" OR "Abstract":pddl OR "Abstract":"formal verification" OR "Abstract":grounding OR "Abstract":hallucination OR "Abstract":"neuro-symbolic")
```

### String 2

```text
("All Metadata":vision OR "All Metadata":visual) AND ("All Metadata":language OR "All Metadata":linguistic) AND (("All Metadata":"Large Language Model" OR "All Metadata":LLM) NEAR/8 ("All Metadata":robot* OR "All Metadata":action)) AND ("All Metadata":Hallucination OR "All Metadata":alignment OR "All Metadata":Grounding)
```

### String 3

```text
((("All Metadata":robot* OR "All Metadata":autonomous) NEAR/5 "All Metadata":mobile) AND (("All Metadata":hospital* OR "All Metadata":clinical) NEAR/5 ("All Metadata":logistics OR "All Metadata":health*)) AND ("All Metadata":ROS* OR "All Metadata":Gazebo))
```

## ACM Digital Library

### String 1

```text
Full-Text:((("large language model" OR LLM) AND robot*) OR (("large language model" OR LLM) NEAR/5 "autonomous agent")) AND (Title:(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic") OR Abstract:(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic"))
```

### String 2

```text
Abstract:(("vision" OR "visual") AND ("language" OR "linguistic")) AND (("Large Language Model" OR "LLM") AND (robot* OR "action")) AND ("Hallucination" OR "alignment" OR "Grounding")
```

### String 3

```text
Anywhere:("Mobile Robot" OR "Autonomous Robot") AND ("Hospital Logistics" OR "Healthcare Environment" OR "Critical Domain") AND ("ROS 2" OR Gazebo)
```
