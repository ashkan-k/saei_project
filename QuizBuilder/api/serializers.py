from rest_framework import serializers
from QuizBuilder.models import QuizQuestion, QuizQuestionChoice, Quiz, UserQuiz, UserQuizQuestionAnswer
from User.api.serializers import UserSerializer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['questions'] = QuizQuestionSerializer(many=True).to_representation(instance.questions.all())

        return rep


class QuizQuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestionChoice
        fields = '__all__'


class QuizQuestionSerializer(serializers.ModelSerializer):
    choices = serializers.ListField(write_only=True)

    class Meta:
        model = QuizQuestion
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        choices = instance.choices.order_by('id')
        rep['choices'] = QuizQuestionChoiceSerializer(many=True).to_representation(
            choices) if choices else None

        return rep

    def save(self, **kwargs):
        choices = self.validated_data.pop('choices')
        instance = super().save()

        choices_list = []
        for item in choices:
            obj, created = QuizQuestionChoice.objects.get_or_create(id=item.get('id'))
            obj.is_answer = item['is_answer']
            obj.text = item['text']
            obj.save()
            choices_list.append(obj)

        instance.choices.set(choices_list)
        return instance


class UserQuizQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizQuestionAnswer
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['question'] = QuizQuestionSerializer().to_representation(instance.question) if instance.question else None
        rep['answer'] = QuizQuestionChoiceSerializer().to_representation(instance.answer) if instance.answer else None
        return rep


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer().to_representation(instance.user) if instance.user else None
        rep['quiz'] = QuizSerializer().to_representation(instance.quiz) if instance.quiz else None

        user_quiz_questions = instance.user_quiz_questions.all()
        rep['user_quiz_questions'] = UserQuizQuestionAnswerSerializer(many=True).to_representation(user_quiz_questions)

        return rep
